j #!/usr/bin/env python
# -*- coding: utf-8 -*-


import address_parser
import argparse
import tools
from datetime import datetime
from importlib import reload
import json
import pandas as pd
import re
import sys
import time


EMAIL_RE = re.compile(
    r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""",
    re.I)


URL_RE = re.compile(
    r'''^(https?:\/\/)?(www\.)?[-a-zA-Z0-9:%._\+~#=]{1,256}\.[a-zA-Z0-9А-ЯЄІЇҐа-яєіїґ()]{1,8}\b([-a-zA-Z0-9():%_\+.~#?&//=]*)$''')

PHONE_RE = re.compile(r"^[0-9\/\\\(\)\-\+]+$")


def german_date_to_iso(date_string):
    # print(f"date_string: {date_string}")
    _ = datetime.strptime(date_string, "%d.%m.%Y")
    return _.date().isoformat()


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(f"--- {round(time.time() - start_time, 2)} seconds ---")
    return wrapper


def add_addresses(df, counter=0):
    region, rajon, locality = [], [], []
    for _, row in df.iterrows():
        # print(row)
        if pd.isnull(row.full_address):
            region.append(None)
            rajon.append(None)
            locality.append(None)
            continue
        try:
            parsed_address = ap.parse_address(row.full_address)
        except KeyError:
            print(f"\n @ {_}\n{row.full_address}")
        except:
            print(f"Unexpected error: {sys.exc_info()[0]}")
            print(row.full_address)
            raise
        o = parsed_address['oblast']
        r = parsed_address['rajon']
        l = parsed_address['locality']
        region.append(o)
        rajon.append(r)
        locality.append(l)
        counter += 1
        if counter % 200000 == 0:
            print(counter, end="; ")
    res = pd.DataFrame(
        {'region': region, 'rajon': rajon, 'locality': locality})
    return res


def get_boss(signers: list) -> str:
    # print("signers INIT", signers)
    boss = None
    if signers is None:
        return boss
    signers_box = []
    try:
        for signer in signers:
            if (m := re.search("(^.+?- (?:підписант|керівник))",
                signer, re.I)) is None: continue
            # m.group(1) це і є рядок
            splitted = [x.strip() for x in m.group(1).split('-')]
            if len(splitted) > 2:
                splitted = [" ".join(splitted[:-1]), splitted[-1]]
            signers_box.append(splitted)
        signers = dict([x[::-1] for x in signers_box])
        # print(signers)
        boss = signers.get('КЕРІВНИК')
        if boss is None:
            # try 2nd
            boss = signers.get('ПІДПИСАНТ')
    except:
        print(signers)
        raise
    else:
        return boss


def get_sex(string):
    if any(
        [string.endswith(x) for x in (
         "ЄВИЧ", "ЕВИЧ", "ОВІЧ", "ОВИЧ", "ЙОВИЧ", "ЛІЧ", "ОГЛИ")]):
        return "m"
    elif any([string.endswith(x) for x in (
        "ОВНА", "ІВНА", "ЄВНА", "ЇВНА", "ІНІЧНА", "КИЗИ", "ГІЗИ",
        "КІЗИ", "ЕВНА")]):
        return "f"
    else:
        name_parts = [x.strip() for x in string.split(" ")]
        if len(name_parts) < 2:
            return "u"
        sex = NAMES_DICT.get(name_parts[1])
        if sex:
            # print(f"found for {string}")
            return(sex)
        return "u"


def parse_contacts(contact_string):
    if not contact_string:
        return None, None
    contact_string = [x.strip() for x in contact_string[0].split(";")]
    _ = [y for y in contact_string if URL_RE.match(y) is None]
    emails = None if not (
        k:=";".join([y for y in _ if EMAIL_RE.match(y) is not None])) else k
    phones = [re.sub("[a-zа-яіїєґ]+", "", x).strip() for x in (y for y in _ if EMAIL_RE.match(y) is None)]
    phones = [y for y in phones if (PHONE_RE.match(y) is not None) and len(y) > 2]
    phones = None if not (z:=";".join(phones)) else z
    return emails, phones


def parse_jsonl(jsonl_filename, active_only=None):
    counter = 0
    out_box = []   # підприємсьво
    kved_box = []  # КВЕД
    founders_box = []  # бенефіціари+завсновники
    with open(jsonl_filename) as edr:
        for line in edr:
            try:
                l = json.loads(line)
            except:
                print(line)
                raise
            # print(l)
            # Обмеження Активних форм
            if active_only:
                if l['stan'] != "зареєстровано":
                    continue
            rec_no = l["record"]
            stan = l["stan"]
            contacts_email, contacts_phone = parse_contacts(l['contacts'])
            if l["facemode"] == 'u':
                kod = l['edrpou']
                # print(kod, l['contacts'], f"E: {contacts_email}\nP: {contacts_phone}")
                boss = get_boss(l['signers'])
                opf = l["opf"]
            else:
                boss = kod = opf = None
            ak_code = ak_name = None
            if l['activity_kinds'] is not None:
                for ak in l['activity_kinds']:
                    primary_ak = 'так' if (ak_prim:=ak.get('primary')) is not None else "ні"
                    kved_box.append(
                        [int(rec_no),
                         ak["code"], ak["name"], primary_ak])
                    if ak_prim == 'так':
                        ak_code, ak_name = ak["code"], ak["name"]
            # дата реєстрації
            reg_date = None
            try:
                registration_info = l['registration']
                paper_date, digi_date = registration_info.get('paper_date'), \
                    registration_info.get('digi_date')
                if any(e is not None for e in (paper_date, digi_date)):
                    min_reg_date = min(datetime.fromisoformat(d) for d in (
                        paper_date, digi_date
                    ) if d is not None)
                    reg_date = min_reg_date.date().isoformat()
            except:
                print(l)
                raise
            # дата припинння
            term_date = l["terminated_info"]["date"]
            if l["facemode"] == 'u':
                # бенеки енеки
                # print(l.get('founders'))
                if l.get('founders') is not None:
                    for founder in l['founders']:
                        # print(founder)
                        founders_box.append(
                            [int(rec_no), founder, 'f'])
                if l.get('beneficiaries') is not None:
                    for beneficiary in l['beneficiaries']:
                        founders_box.append(
                            [int(rec_no), beneficiary, 'b'])
            try:
                # рядок формується остаточно ТУТ
                csv_line = (l['facemode'], int(rec_no), kod, opf, reg_date,
                            term_date, l['name'], boss, ak_code, ak_name,
                            l["address"], stan, contacts_email, contacts_phone)
            except TypeError:
                print(l)
                raise
            out_box.append(csv_line)
            counter += 1
            if counter % 40000 == 0:
                print(counter, end="; ")
    print(len(out_box))
    return out_box, kved_box, founders_box


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='+', help="JSONL files")
    parser.add_argument("--active", action='store_true',
                        help="parse only active")
    parser.add_argument("--address", action='store_true',
                        help="parse addresses")
    args = parser.parse_args()
    jsonl_files = args.files
    entity_total = []
    kved_total = []
    founders_total = []

    start_time = time.time()
    for name in jsonl_files:
        # print(len(entity_total))
        entity, kved, founders = parse_jsonl(
            name,
            active_only=args.active)
        entity_total.extend(entity)
        kved_total.extend(kved)
        founders_total.extend(founders)
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")

    df = pd.DataFrame.from_records(
        entity_total,
        columns=['facemode', 'rec_no', 'edrpou', 'opf', 'reg_date',
                 'term_date', 'name', 'boss', 'kved', 'kved_uk', "full_address",
                 'stan', 'contacts_email', 'contacts_phone'])
    df_kved = pd.DataFrame.from_records(
        kved_total, columns=['rec_no', 'kved', 'kved_name', 'primary'])
    df_founders = pd.DataFrame.from_records(
        founders_total, columns=['rec_no', 'subject', 'type'])

    df_kved.to_parquet("df_kved.parquet")
    df_founders.to_parquet("df_founders.parquet")
    df.to_parquet("df.parquet")
    print("JSONL file(s) parsed.")

    df['region'] = None
    df['rajon'] = None
    df['locality'] = None

    if not args.address:
        print("No option for address parsing is passed.")
        sys.exit(0)

    # reload(address_parser)
    print('Start address parsing...')
    ap = address_parser.LightAddressParser(
        np_marks=tools.marks, obl_marks2=tools.obl_marks2,
        obl_marks=tools.obl_marks)

    # @timer
    # counter = 0
    start_time = time.time()
    df[['region', 'rajon', 'locality']] = add_addresses(df)
    print(f"\n--- {round(time.time() - start_time, 2)} seconds ---")
    print('Saving file...', end='')
    df.to_parquet("df.parquet")
    print('saved\n')
