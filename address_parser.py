# !/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO:
# що робити з
# М. ІВАНО-ФРАНКІВСЬК С.УГОРНИКИ

import re
import logging
from typing import Optional
import rajons
import tools
from importlib import reload

reload(rajons)

LOG_LEVEL = logging.INFO

logging.info(f"Log level is: {'DEBUG' if LOG_LEVEL == 10 else 'INFO'}")

if LOG_LEVEL == 10:
    import test_set

logging.basicConfig(filename='address_parser.log', filemode='w',
                    format='%(asctime)s - %(message)s',
                    level=LOG_LEVEL)
obl_etalon = list(tools.obl_marks.values())


class LightAddressParser(object):
    def __init__(self, np_marks=None, obl_marks=None, obl_marks2=None, ):
        self.LOWER_UK = "а-яєїіґ"
        self.UPPER_UK = self.LOWER_UK.upper()
        self.marks = np_marks
        self.obl_marks = obl_marks
        self.obl_marks2 = obl_marks2

    @staticmethod
    def _bad_oblast_fix(addr_string: list) -> Optional[str]:
        _ = [x.split() for x in addr_string]
        _ = [item for sublist in _ for item in sublist]
        _ = [x for x in _ if 8 >= len(x) > 5 and tools.levenshtein(
            x, "ОБЛАСТЬ") <= 2]
        if _:
            # є погана область
            return _[0]
        return

    @staticmethod
    def _clean_commas(addr_string):
        # [,.\s]+
        k = re.sub(r"^[\s,.]+", "", addr_string)
        return k.strip()

    @staticmethod
    def _check_sp_city(string: Optional[str]) -> Optional[str]:
        """
        Перевірка міст зі спецстатустом
        :param string: населений пункт для перевірки
        :return: None, якщо це не місто спецстатусу, інакше -- місто, до якого
        додано "М. " спереду
        """
        if re.match(r"(?:^М.\s)?(КИЇВ|СЕВАСТОПОЛЬ)$", string) is not None:
            if not string.startswith("М"):
                string = "М. " + string
            return string
        return

    @staticmethod
    def _remove_reverse(addr_dict):
        if addr_dict['oblast'] is None and addr_dict['rajon'] is None:
            return {"changed": False, "string": None}
        repl_res = addr_dict['addr_string']
        repl_obl = None
        if addr_dict['oblast'] is not None:
            repl_obl = re.sub(r"ОБЛ(?:\.|АСТЬ) " + addr_dict['oblast'], "",
                              addr_dict['addr_string'])
        if addr_dict['rajon'] is not None:
            _ = repl_obl if repl_obl is not None else addr_dict['addr_string']
            repl_res = re.sub("Р-Н " + re.sub(" Р-Н$", "", addr_dict['rajon']),
                              "", _)
        return {"changed": repl_res != addr_dict['addr_string'],
                "string": repl_res}

    @staticmethod
    def rajon_fix(pure_raj_name):
        for r in rajons.raj_etalon[pure_raj_name[:1]]:
            dist = tools.levenshtein(r, pure_raj_name)
            if dist <= 2:
                return {'changed': True, 'raj_name': r + " Р-Н"}
        return {'changed': False, 'raj_name': None}

    def _satanize(self, addr_string, **kwargs):
        addr_string = addr_string.upper()
        # TODO
        # 25 км вичищати тут
        if LOG_LEVEL == 10:
            print(f"==> {addr_string}")
        scheme = None
        weird_address_re = re.compile(r"^.+?УКРАЇНА$", re.I)
        if weird_address_re.match(addr_string) is not None:
            # weird_address_re will match:
            # 94400, КОМІНТЕРНА, 3А, 0, 0, КРАСНОДОН, 0, ЛУГАНСЬКА, УКРАЇНА
            scheme = "index-uk"
        marks = obl_marks = obl_marks2 = None
        if (m1 := kwargs.get('obl_marks')) is not None:
            obl_marks = m1
        if (m2 := kwargs.get('obl_marks2')) is not None:
            obl_marks2 = m2
        if (m0 := kwargs.get('marks')) is not None:
            marks = m0
        addr_string = tools.digits_up(addr_string)
        addr_string = re.sub(r"([ЛЬНЙ])/([А-ЯЄЇҐІ])", r"\1, \2", addr_string, re.I)
        addr_string = re.sub(r"-+,", "", addr_string)
        addr_string = re.sub(r"(?:\s+?)?[‒–—―-](?:\s+?)?", "-", addr_string)
        addr_string = re.sub(r"[\'”]", "’", addr_string)
        addr_string = re.sub(r"(\s|\b)с(\.|\b)", ", с. ", addr_string)
        addr_string = re.sub(r"(?<!\d)\s?[0-],", "", addr_string)
        for k, v in marks.items():
            addr_string = re.sub(r'\b' + k + r'(\b|,)', v, addr_string, re.I)
        for k, v in obl_marks.items():
            addr_string = re.sub(k, v, addr_string)
        for k, v in obl_marks2.items():
            addr_string = re.sub(r'\b' + k + r'\b', v, addr_string)
        # TODO:
        # розділити по комах, зробити операції і зібрати
        addr_string = re.sub(r"\s+", " ", addr_string)
        addr_string = re.sub(r"\(\s", r"(", addr_string)
        addr_string = re.sub(r"\s\)", r")", addr_string)
        addr_string = re.sub(r"(?<=\.)(\w)", r" \1", addr_string)
        addr_string = re.sub(r"\([^)].+?\)", "", addr_string)
        # з розбивкою
        split_addr = [x.strip() for x in addr_string.split(',')]
        split_addr = [x for x in split_addr if re.match(
            r"\d(?!\d)\s?-?.+?МКР.+?$", x) is None]
        split_addr = [
            re.sub(r"^" + tools.trailing_comma_re, "", x) for x in split_addr]
        wrong_obl = self._bad_oblast_fix(split_addr)
        addr_string = ",".join(split_addr)
        # нове виправлення областей
        if wrong_obl is not None:
            addr_string = re.sub(wrong_obl, "ОБЛАСТЬ", addr_string)
        logging.debug(f"{'-' * 10} RECORD sanity: {addr_string}")
        return {"addr_string": addr_string, "scheme": scheme,
                'sp_city': False, 'double_city': False, 'city_rajon': None}

    def _extrart_obl(self, sanitized):
        logging.debug("--> Пошук області")
        # print(sanitized)
        str_types_re = re.compile(r"^" + tools.str_types_re_str)
        str_office_re = re.compile(r"^" + tools.office_types_re_str, re.I)
        addr_string = sanitized['addr_string']
        # тимчасовий рядок для заміни вулиць, назви які виглядають як
        # назви областей
        temp_addr_string = [x.strip() for x in addr_string.split(",")]
        for h in tools.house_parts:
            re_house_str_reverse = r"^.+?" + h + r"\b"
            re_house_str = r"^" + h + r"\s.+?$"
            temp_addr_string = [x for x in temp_addr_string if re.match(
                re_house_str, x, flags=re.I) is None]
            temp_addr_string = [x for x in temp_addr_string if re.match(
                re_house_str_reverse, x, flags=re.I) is None]
        temp_addr_string = ", ".join(temp_addr_string)
        logging.debug(f"temp_addr_string: {temp_addr_string}")
        # oblasts_v3 -- шаблон регулярного виразу для назв областей та міст,
        # що мають спеціальний статус
        re_oblasts3 = re.compile(tools.oblasts_v3, flags=re.I)
        all_oblasts = re_oblasts3.findall(temp_addr_string)
        logging.debug(f"Багато областей{all_oblasts}")
        # пошук міста обласного значення
        sp_city = [x for x in all_oblasts if self._check_sp_city(x) is not None]
        logging.debug("пошук міста обласного значення")
        # logging.debug(sp_city)
        if not sp_city:
            logging.debug("Не знайшли")
        else:
            logging.debug(f"sp_city: {sp_city}")
            sanitized['sp_city'] = True
            # obl_string = sp_city[0]
        if not all_oblasts:
            logging.debug("NOT FOUND by regexp: None")
            obl_string = None
        else:
            obl_string = all_oblasts[0]
        if obl_string is not None:
            addr_string = re.sub(
                obl_string + r"(?:\sОБЛ\.)?", "", addr_string, count=1)
            obl_string = re.sub(r"\bОБЛ\.?$", "", obl_string)
            obl_string = obl_string.strip()
            logging.debug(f"obl string is: '{obl_string}'")
            if (sp := self._check_sp_city(obl_string)) is not None:
                logging.debug(f"Знайдено місто спец статус: {obl_string}!!!")
                sanitized['sp_city'] = True
                obl_string = sp
        if obl_string is None:
            logging.debug("TRY: guess oblast")
            splitted_addr = [y for x in sanitized['addr_string'].split(',')
                             if (y := x.strip())]
            splitted_addr = [x for x in splitted_addr
                             if not re.search(r"^\d", x)]
            splitted_addr = [x for x in splitted_addr
                             if not str_types_re.search(x)]
            splitted_addr = [x for x in splitted_addr
                             if not str_office_re.search(x)]
            splitted_addr = [x for x in splitted_addr
                             if not re.search(tools.raj_re, x)]
            logging.debug(f"Splitted is: {splitted_addr}")
            match_index = 100
            match_str = bad_obl = None
            for o in obl_etalon:
                for i in splitted_addr:
                    # if re.match("^М\.", i):
                    #    is_city = True
                    i = re.sub(r"^М\.\s", "", i)
                    if i[0] != o[0]:
                        continue
                    i = re.sub(r"(^ОБЛ.?\s?|\sОБЛ.?$)", "", i)
                    lev_index = tools.levenshtein(i, o)
                    if lev_index < match_index:
                        match_index = lev_index
                        match_str = o
                        bad_obl = i
            # 4 достатньо, єдина область, на яку так можна випадково вийти, це
            # ХАРКІВ + СЬКА (4)
            if match_index <= 4:
                # print(bad_obl)
                logging.debug(f"Levenstein FOUND MATCH: {match_str} with "
                              "index {match_index}")
                if match_str in ("СЕВАСТОПОЛЬ", "КИЇВ"):
                    match_str = "М. " + match_str
                    sanitized['sp_city'] = True
                obl_string = match_str
                if bad_obl not in ["ХАРКІВ"]:
                    addr_string = re.sub(bad_obl, "", addr_string)
            del match_str
        sanitized['oblast'] = obl_string
        logging.debug(f"{'-' * 10} Остаточна ОБЛАСТЬ: {obl_string}")
        splitted = [y.strip() for y in addr_string.split(',')]
        splitted = [x for x in splitted if re.match(r'^ОБЛ\.$', x) is None]
        splitted = [re.sub(r"’(?P<raj_name>.+)’",
                           r'\g<raj_name>', x) for x in splitted]
        addr_string = ",".join(splitted)
        sanitized['addr_string'] = addr_string
        # print(sanitized)
        return sanitized

    def _extrart_raj(self, obl_data):
        logging.debug("--> Пошук РАЙОНУ")
        logging.debug(f"Вхідні дані: {obl_data}")
        raj_string = None
        raj_regex = fr"""[{self.UPPER_UK}][{self.LOWER_UK}\’\']+(?:-[{self.UPPER_UK}][{self.LOWER_UK}\’\']+)?\sр-н"""
        if obl_data['sp_city']:
            if (sp_raj := rajons.city_rajons.get(obl_data['oblast'])) is not None:
                sp_raj_regexp = "(" + "|".join(sp_raj) + ")"
                if (m := re.search(
                        sp_raj_regexp, obl_data['addr_string'],
                        flags=re.I)) is not None:
                    logging.debug("Знайдено район міста спец.статус")
                    obl_data['city_rajon'] = m.group(0) + " Р-Н"
            logging.debug("Місто спецстатус, далі")
            obl_data["rajon"] = raj_string
            return obl_data
        oblast = obl_data["oblast"]
        obl_data['double_city'] = False
        addr_string = obl_data["addr_string"]
        splitted = [y for x in addr_string.split(",") if (y := x.strip())]
        reverse_raj_re = r"(Р-Н\s(?P<rev_raj>.+$))"
        reverse_raj = [y for x in splitted if (y := re.match(
            reverse_raj_re, x)) is not None]
        if reverse_raj:
            logging.debug("Наркомансько-реверсивний район -- присутній")
            raj_string = reverse_raj[0].group("rev_raj")
        # splitted = [x for x in splitted if re.match(r'^ОБЛ\.$', x) is None]
        # print(splitted)
        raj_regex2 = r"[А-ЯЄЇІҐ][а-яєїіґ’\'\s]+(?:-[А-ЯЄЇІҐ][а-яєїіґ’\']+)?\sр-н"
        if k := [y.group(0) for x in splitted if (y := re.match(
                raj_regex2, x, flags=re.I)) is not None]:
            raj_string = k[0]
        elif (m := re.search(raj_regex, addr_string, re.I)) is not None \
                and oblast is not None:
            raj_string = m.group(0)
        elif oblast is not None:
            logging.debug(f"Є область, нема району {splitted}")
            obl_rajons = rajons.rajons_oblast[re.sub(r"^М\.\s", "", oblast)]
            guess_raj = list(set(obl_rajons) & set(splitted))
            logging.debug(f"Знайдено район(и) в переліку {guess_raj}")
            if guess_raj and len(guess_raj) == 1:
                # перевіряємо, чи назв, по яких співпадають місто та район --
                # 2 шт. Якщо їх 2, одна з них стає районом, інший -- містом
                # якщо 1 -- це місто
                if guess_raj[0] in rajons.double_cities:
                    obl_data['double_city'] = True
                    logging.debug("Назва міста і р-ну співпали")
                    if splitted.count(guess_raj[0]) == 2:
                        addr_string = re.sub(
                            guess_raj[0], "", addr_string, count=1)
                        raj_string = guess_raj[0] + " Р-Н"
                    else:
                        raj_string = None
                else:
                    # print(guess_raj)
                    raj_string = guess_raj[0] + " Р-Н"
        if raj_string is not None:
            # print(raj_string)
            pure_raj_name = re.sub(" Р-Н$", "", raj_string)
            # Шукаємо в еталонному переліку районів України район для
            # звірки. Неправильну назву буде замінено правильною
            try:
                raj_collection = rajons.raj_etalon[raj_string[:1]]
            except KeyError:
                raj_collection = []
            if not raj_collection:
                raj_string = None
            elif pure_raj_name not in raj_collection:
                logging.debug(f"Назва '{raj_string}' відсутня "
                              "в довіднику районів")
                fix_result = self.rajon_fix(pure_raj_name)
                if fix_result['changed']:
                    raj_string = fix_result['raj_name']
                    # їмовірність існування у рядку ще одного такого ж
                    # значення з помилкою вкрай низька, тому просто замінюємо
                    addr_string = re.sub(pure_raj_name, raj_string, addr_string)
                    logging.debug(f"Заміна: {pure_raj_name} => {raj_string}")
        logging.debug(f"{'-' * 10} Остаточний РАЙОН: {raj_string}")
        if raj_string is not None:
            # Вінниця Академ район fix
            raj_string = re.sub(
                tools.str_types_re_str + ".+?$", "", raj_string).strip()
            addr_string = re.sub(
                "(?:Р-Н )?" + raj_string + "(?: Р-Н)?", "", addr_string)
            # print(addr_string)
        obl_data["rajon"] = raj_string
        obl_data['addr_string'] = addr_string
        logging.debug(f"{'=' * 10} RAJON out: {raj_string}")
        return obl_data

    @staticmethod
    def _extract_zip(obl_data):
        addr_string = obl_data["addr_string"]
        re_zip = re.compile(r"^(\d{5})\D|\D(\d{5})\D|\D(\d{5})$")
        if (m := re.search(re_zip, addr_string)) is None:
            return obl_data
        zip_string = [x for x in m.groups() if x is not None]
        addr_string = re.sub(zip_string[0], "", addr_string)
        obl_data["zip"] = zip_string[0]
        obl_data["addr_string"] = addr_string
        return obl_data

    def _extract_np(self, zip_data):
        # видалення реверсивних АТО
        logging.debug(f"Вхідні дані: {zip_data}")
        reverse_str_fix = self._remove_reverse(zip_data)
        # print(reverse_str_fix)
        if reverse_str_fix['changed']:
            logging.debug(f"Пошук реверсивних рядків успішний: "
                          f"{reverse_str_fix}")
            zip_data['addr_string'] = reverse_str_fix['string']
        locality = city_rajon = None
        re_np = re.compile(r"(\b(?:(?<!ВУЛ\.\s)М\.|С\.|СМТ|С-ЩЕ)(?:\s+)?(?!,).+?\b)(?:,|$)", flags=re.I)
        addr_string = zip_data['addr_string']
        logging.debug(f"{'-' * 10} НАСЕЛЕНИЙ ПУНКТ")
        if zip_data['sp_city']:
            logging.debug(f"Місто спец статус, завершено")
            zip_data["locality"] = zip_data['oblast']
            return zip_data
        if zip_data['double_city'] and zip_data['rajon'] is not None:
            rajon = zip_data['rajon']
            if re.match(r"^.+?ИЙ Р-Н$", rajon, re.I):
                locality = re.sub(" Р-Н$", "", rajon, re.I)
            zip_data["locality"] = locality
            return zip_data
        addr_string = re.sub("[, ]{2,}", ',', addr_string)
        addr_string = re.sub(r"^[,-.\s]+", '', addr_string)
        addr_string = re.sub(" +", ' ', addr_string)
        splitted = [self._clean_commas(y.strip()) for y in
                    addr_string.split(",") if y]
        oblast = zip_data['oblast']
        rajon = zip_data['rajon']
        if rajon is not None:
            splitted = [y for x in splitted if (
                y := re.sub(rajon + r"(?: Р-Н)?$", "", x).strip())]
        if oblast is not None:
            splitted = [re.sub(oblast + r"(?: ОБЛ\.)?", "", x, re.I)
                        for x in splitted]
        splitted = [re.sub(tools.str_types_re_str + r".+?$", "", x, re.I)
                    for x in splitted]

        splitted = [y for x in splitted if (y := self._clean_commas(x))]
        splitted = [re.sub(tools.office_types_re_str + r".+?$",
                           "", x, flags=re.I) for x in splitted]
        splitted = [re.sub(r"^\d+$", "", x, flags=re.I) for x in splitted]
        splitted = [x for x in splitted if x]
        if len(splitted) == 1:
            locality = splitted[0]
        elif not splitted:
            # No locality at all
            zip_data['locality'] = None
            return zip_data
        else:
            if zip_data['scheme'] == "index-uk":
                logging.debug("Схема index-uk")
                splitted = splitted[::-1]
                logging.debug(f"Рядок розбито: {splitted}")
        if zip_data['oblast'] in rajons.oblasts_has_raion_cities:
            # якщо зазначено область і ця область має міста
            # районного значення
            in_city_raions = list(
                rajons.city_rajons.get(zip_data['oblast']).keys())
            np_with_city_raions = list(
                set(rajons.city_rajons.get(zip_data['oblast']).values()))
            # чи дійсно шснує н. п. у рядку, який містить райони?
            raj_container = []
            for np in np_with_city_raions:
                _ = [x for x in splitted if re.match(
                    r"^(.+)?" + np + r"$", x) is not None]
                if _:
                    raj_container.extend(_)
            if not raj_container:
                logging.debug("кандидати на НП з райподілом відсутні")
                locality = splitted[0]
            else:
                if zip_data['rajon'] is not None:
                    city_rajon_name = re.sub(r"\s+Р-Н?$", "", zip_data['rajon'])
                    splitted += [city_rajon_name]
                logging.debug(f"raj_container: {raj_container}")
                logging.debug(f"np_with_city_raions {np_with_city_raions}")
                logging.debug(f"in_city_raions {in_city_raions}")
                logging.debug(f"Шукаємо серед: {splitted}")
                rajon_v_m = [r for r in splitted if re.sub(" Р-Н$", "", r) in
                             in_city_raions]
                if rajon_v_m:
                    logging.debug(f"місто має район {rajon_v_m}")
                    city_rajon = rajon_v_m[0] + " Р-Н"
                    zip_data['rajon'] = None
                    splitted = [x for x in splitted if x not in [rajon_v_m[0],
                                                                 city_rajon]]
                    splitted = [x for x in splitted if re.match(
                        "^(.+)?ОБЛАСТЬ", x, flags=re.I) is None]
                logging.debug(f"Розбивка: {splitted}")
                if splitted:
                    locality = splitted[0]
        else:
            # якщо область НЕ має міст з райподілом
            city_raj = [x for x in splitted if re.match(tools.raj_re, x)]
            tmp_city = [x for x in splitted if re.match(tools.city_start_re, x)]
            # print(city_raj , tmp_city)
            if city_raj and tmp_city:
                city_raj_str = re.sub(r"\s+Р-Н?$", "", city_raj[0])
                tmp_city_str = re.sub(tools.city_start_re, "", tmp_city[0])
                if rajons.city_rajons2.get(city_raj_str):
                    if tmp_city_str in rajons.city_rajons2[city_raj_str]:
                        locality = tmp_city_str
                        city_rajon = city_raj_str
            elif tmp_city and zip_data['rajon'] is not None:
                guess_city = re.sub(r"^М\.", "", tmp_city[0]).strip()
                city_raj_str = re.sub(r"\s+Р-Н?$", "", zip_data['rajon'])
                if (raj_list := rajons.city_rajons2.get(city_raj_str)) is not None:
                    if guess_city in raj_list:
                        locality = "М. " + guess_city
                        city_rajon = city_raj_str + " Р-Н"
                        zip_data['rajon'] = None
            # else:
            # TODO
        if locality is None:
            # print("!2", splitted)
            # print([re_np.match(x) for x in splitted])
            if matches := [y for x in splitted
                           if (y := re_np.match(x)) is not None]:
                np = matches[0].group(0)
                if self._check_sp_city(np):
                    zip_data['sp_city'] = True
                locality = np
        if locality is None:
            # мабуть найслабша частина :(
            rajons_in = [x for x in splitted
                         if re.match(tools.raj_re, x) is not None]
            if rajons_in:
                # визначаємо рядок, схожий на р-н, який буде збережено, якщо їх
                # таких більше ніж два
                untouch_raj = rajons_in[0]
            else:
                untouch_raj = None
            if len(splitted) > 1:
                splitted = [x for x in splitted
                            if re.search(tools.oblasts_v3, x) is None]
                # print("!",splitted)
                # print(zip_data)
                locality_vars = []
                if not zip_data['double_city']:
                    if splitted.count(untouch_raj) == 1:
                        for x in splitted:
                            if rajons.raj_etalon.get(x[:3]) is None:
                                locality_vars.append(x)
                                continue
                            if x not in rajons.raj_etalon[x[:3]]:
                                locality_vars.append(x)
                    # print("splitted", splitted)
                    if locality_vars:
                        locality = locality_vars[0]  # splitted[0]
                else:
                    locality = splitted[0]
        else:
            if re.match(tools.np_digit_re, locality):
                logging.debug("Місто закінчується цифрою")
                locality = re.sub(r"[\s-]+\d+$", "", locality)
        zip_data['locality'] = locality
        zip_data['city_rajon'] = city_rajon
        return zip_data

    def parse_address(self, addr_string):
        sanitized = self._satanize(
            addr_string, marks=self.marks, obl_marks=self.obl_marks,
            obl_marks2=self.obl_marks2)
        parsed_address = self._extrart_obl(sanitized)
        parsed_address = self._extrart_raj(parsed_address)
        parsed_address = self._extract_zip(parsed_address)
        parsed_address = self._extract_np(parsed_address)
        if LOG_LEVEL != logging.DEBUG:
            del parsed_address['sp_city']
            del parsed_address['scheme']
            del parsed_address['double_city']
        del parsed_address['addr_string']
        logging.debug(f"{'>' * 10} RECORD OUT: {parsed_address}")
        logging.debug(f"{'-' * 80}")
        if LOG_LEVEL == logging.DEBUG:
            print(f"<== {parsed_address}")
        return parsed_address


if __name__ == '__main__':
    ap = LightAddressParser(np_marks=tools.marks, obl_marks2=tools.obl_marks2,
                            obl_marks=tools.obl_marks)
    if LOG_LEVEL == 10:
        try:
            for test_item in test_set.test:
                assert ap.parse_address(test_item[0]) == test_item[1]
        except AssertionError:
            raise
    print(ap.parse_address("Україна, 50048, Дніпропетровська обл., місто Кривий Ріг, ПАРОВОЗНА, будинок 54"))
    print(ap.parse_address("89600, ДУЛІШКОВИЧА, 1, МУКАЧЕВО, ЗАКАРПАТСЬКА, УКРАЇНА"))
    print(ap.parse_address("09113, ВУЛИЦЯ ЩОРСА, 81-А, 50, БІЛА ЦЕРКВА, БІЛА ЦЕРКВА, КИЇВСЬКА, УКРАЇНА"))
    print(ap.parse_address("67624, ОДЕСЬКА ОБЛ., БІЛЯЇВСЬКИЙ РАЙОН, СЕЛО ДАЧНЕ, 25 КМ ШОСЕ ОДЕСА-КИЇВ"))
    print(ap.parse_address("65074, ВУЛ.В.ТЕРЕШКОВОЇ, БУД.26, КВ.57, М.ОДЕСА, ОДЕСЬКА ОБЛАСТЬБ, УКРАЇНА"))
    print(ap.parse_address("21003, ДИМИТРОВА, 41 А, ВІННИЦЯ, _, ВІННИЦЬКА, УКРАЇНА"))
    # print(ap.parse_address("85000, ДОНЕЦЬКА ОБЛ., МІСТО ДОБРОПІЛЛЯ, ВУЛИЦЯ ПЕРШОТРАВНЕВА, РАЙОН 2-Ї ТА 3-Ї, КОТЕЛЬНИХ"))
