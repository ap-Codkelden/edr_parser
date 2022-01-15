#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import json
import argparse
from datetime import datetime
import pandas as pd
from tools import *


# TODO:
# * make data directory
# * stream compression
# data URL https://data.gov.ua/dataset/1c7f3815-3259-45e0-bdf1-64dca07ddc10/resource/266bfef3-6d69-4e17-9f69-a5edf7db6ad2

GER_DATE_LONG = re.compile(r"^\d{2}\.\d{2}\.\d{4}$")
# REG_NO = re.compile(r"^\d+$")
REG_NO = re.compile(r"^[\d_]+$")


# 11.11.2004; 12271230000000926
def german_date_to_iso(date_string):
    # print(f"date_string: {date_string}")
    _ = datetime.strptime(date_string, "%d.%m.%Y")
    return _.date().isoformat()


def get_fop_terminated_info(terminated_info_string):
    try:
        term_info = [x.strip() for x in terminated_info_string.split(';')]
        if all([REG_NO.match(x) is None for x in term_info]):
            # reg number is absent
            term_date, term_reason = term_info
            term_num = None
        else:
            term_date, term_num, term_reason = term_info
    except Exception as e:
        print(terminated_info_string)
        raise e
    else:
        term_date = german_date_to_iso(term_date)
        return term_date, term_num, term_reason
 

def get_reg_causes(registration_string, to_iso=None):
    paper_date = reg_date = reg_activity = None
    reg_parts = [x.strip() for x in registration_string.split(";")]
    date_parts = [y.group(0) for x in reg_parts if (y:=GER_DATE_LONG.match(x.strip())) is not None]
    try:
        if len(date_parts) == 1:
            reg_date = german_date_to_iso(date_parts[0])
        elif len(date_parts) == 2:
            paper_date, reg_date = (german_date_to_iso(x) for x in date_parts)
        # paper_date, reg_date = [german_date_to_iso(x) for x in reg_parts[:2]]
        #if len(reg_parts) == 3:
        #    reg_activity = reg_parts[-1]
        reg_activity = reg_parts[-1]
    except:
        print(registration_string)
        raise
    return paper_date, reg_date, reg_activity


def get_stan(record):
    # print(record)
    # Дата запису про державну реєстрацію припинення
    if (date_term := record['terminated_info']['date']) is not None:
        date_term = datetime.strptime(date_term, "%Y-%m-%d")
    else:
        date_term = None
    # Дата запису про відміну державної реєстрації припинення
    if (date_term_cancel := record['termination_cancel_info']['date']) is not None:
        date_term_cancel = datetime.strptime(date_term_cancel, "%Y-%m-%d")
    else:
        date_term_cancel = None
    # порівняння дат і всього такого
    if all([x is None for x in (date_term, date_term_cancel)]):
        return "зареєстровано"
    elif date_term_cancel is None and date_term is not None:
        return "припинено"
    elif all([x is not None for x in (date_term, date_term_cancel)]):
        if date_term > date_term_cancel:
            return "припинено"
        elif date_term <= date_term_cancel:
            return "в стані припинення"


class ParseEdrpou:
    counter = 0

    @classmethod
    def fast_iter(cls, context, func, *args, **kwargs):
        # print(kwargs)
        """
        http://lxml.de/parsing.html#modifying-the-tree
        Based on Liza Daly's fast_iter
        http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
        See also http://effbot.org/zone/element-iterparse.htm
        """
        # kwargs = kwargs
        for event, elem in context:
            cls.counter += 1
            dry_run = kwargs['dry_run']
            # records_box
            kwargs['counter'] = cls.counter
            func(elem, *args, **kwargs)
            # It's safe to call clear() here because no descendants will be
            # accessed
            elem.clear()
            # Also eliminate now-empty references from the root node to elem
            for ancestor in elem.xpath('ancestor-or-self::*'):
                while ancestor.getprevious() is not None:
                    del ancestor.getparent()[0]
        del context
        return cls.counter


def check_obj_equal(includes):
    inc_keys = [list(k.keys())[0] for k in includes]
    if len(set(inc_keys)) <= 1:
        return True
    return False


def check_obj_equal2(includes):
    if len(set(includes)) <= 1:
        return True
    return False


def extract_data_from_element(element):
    tag = element.tag.lower()
    if len(element) == 0:
        return {tag: element.text}
    includes = [extract_data_from_element(c) for c in element]
    if not check_obj_equal(includes):
        return {k: v for dictionary in includes for k, v in dictionary.items()}
    check_list_keys = [list(k.keys()) for k in includes]
    flat_list = [item for cl in check_list_keys for item in cl]
    if check_obj_equal2(flat_list):
        check_list_values = [list(k.values()) for k in includes]
        return {tag: [x for y in check_list_values for x in y]}
    return {tag: includes}


def post_process(record):
    # addr_parser = LightAddressParser(
    #     np_marks=marks, obl_marks=obl_marks,
    #     obl_marks2=obl_marks2)
    # TODO:
    # всі інші дати перетворити на ISO 8601
    new_term_info = {}
    new_reg_info = {}
    new_term_cancel_info = {}
    if record['address'] is not None:
        record['address'] = csv_compatible(record['address'])
    if record["terminated_info"] is not None:
        new_term_info["date"], new_term_info["number"],\
            new_term_info["reason"] = get_fop_terminated_info(record["terminated_info"])
    else:
        new_term_info = {k: None for k in ["date", "number", "reason"]}
    record["terminated_info"] = new_term_info

    # EXCHANGE_DATA
    _ = record.get("exchange_data")
    if _ is not None:
        for ex_answer in _:
            if (sd:=ex_answer.get("start_date")) is not None:
                ex_answer["start_date"] = german_date_to_iso(sd)
            if (ed:=ex_answer.get("end_date")) is not None:
                ex_answer["end_date"] = german_date_to_iso(ed)

    if record["registration"] is None:
        new_reg_info = {k: None for k in ["paper_date", "digi_date", "number"]}
    else:
        new_reg_info["paper_date"], new_reg_info["digi_date"], new_reg_info["number"] = \
            get_reg_causes(record["registration"], to_iso=True)
    record["registration"] = new_reg_info
    # контакти
    record["contacts"] = [] if record["contacts"] is None else \
        [y for contact in record["contacts"].split(',') if (y := contact.strip())]

    if record["termination_cancel_info"] is None:
        new_term_cancel_info = {k: None for k in ["date", "number", "reason"]}
    else:
        new_term_cancel_info["date"], new_term_cancel_info["number"], \
        new_term_cancel_info["reason"] = get_fop_terminated_info(record["termination_cancel_info"])
    record["termination_cancel_info"] = new_term_cancel_info
    if record['facemode'] == 'u':
        if record['short_name'] is None:
            record['short_name'] = csv_compatible(record['name'])
        # if record['name'] is None:
        #     record['name'] = record['short_name']
        # TODO:
        # пробіли у ПІБ
        if record['signers'] is not None:
            new_signers = []
            for signer in record['signers']:
                new_signers.append(csv_compatible(signer))
            record['signers'] = [s.upper() for s in new_signers]
    else:
        record['stan'] = get_stan(record)
        record['short_name'] = csv_compatible(record['name'])


def process_element(elem, **kwargs):
    record_num = elem.get('record')
    interval = 10000
    counter = kwargs['counter']
    out_file = kwargs['out_file']
    dry_run = kwargs['dry_run']
    # box = kwargs['records_box']
    global box
    record = {"record": record_num, "facemode": kwargs['facemode']}
    for element in elem:
        extracred = extract_data_from_element(element)
        record.update([x for x in extracred.items()])
    post_process(record)
    box.append(record)
    if counter % 100000 == 0:
        print(counter)
        try:
            out_file.write(
                "\n".join([json.dumps(x, ensure_ascii=False) for x in box]) + '\n')
        except:
            raise
        else:
            box = []
    if dry_run:
        return
    # out_file.write(json.dumps(record, ensure_ascii=False, ) + "\n")
    return


if __name__ == '__main__':
    dry_run = False
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', help="XML files")
    args = parser.parse_args()
    xml_files = args.files
    for xml_file in xml_files:
        facemode = 'u' if 'UO' in xml_file else 'f'
        print(facemode)
        out_file = open(f"edr_data_{facemode}.jsonl", "w")
        box = []

        context = etree.iterparse(xml_file, tag='SUBJECT')
        try:
            parsed = ParseEdrpou.fast_iter(
                context, process_element, facemode=facemode, out_file=out_file,
                dry_run=dry_run)
        except:
            raise
        else:
            print("No Errors\n")
        out_file.write(
            "\n".join([json.dumps(x, ensure_ascii=False) for x in box]) + '\n')
        out_file.close()
