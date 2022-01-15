#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd
import re
from typing import Optional


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def unlatin(string):
    if not string or string is None:
        return
    string = string.upper()
    trans_table = str.maketrans({
        "A": "А", "E": "Е", "I": "І", "X": "Х", "O": "О",
        "B": "В", "C": "С", "P": "Р", "M": "М", "H": "Н",
        "T": "Т", "K": "К"})
    return string.translate(trans_table)


def digits_up(string):
    if not string or string is None:
        return
    trans_table = str.maketrans({"@": "2", "#": "3", "$": "4", "%": "5", "^": "6",
                                 "&": "7", "*": "8"})
    return string.translate(trans_table)


'''def csv_compatible(string: str) -> Optional[str]:
    # re.sub(pattern, repl, string, count=0, flags=0)
    if not string or string is None:
        return
    k = string.replace('\xa0', ' ')\
        .replace('"', '”')\
        .replace("'", '’')
    k = re.sub("&nbsp;?", "", k)
    k = re.sub(r"\s+", " ", k)
    return k.strip()'''


def csv_compatible(string: str) -> Optional[str]:
    # re.sub(pattern, repl, string, count=0, flags=0)
    transpose = str.maketrans("aeiopcxBKMHTyAEIOPCX", "аеіорсхВКМНТуАЕІОРСХ")
    if not string or pd.isnull(string):
        return
    k = string.replace('\xa0', ' ').replace('"', '”')\
        .replace("'", '’')
    k = re.sub("&nbsp;?", " ", k)
    k = re.sub("\s+", " ", k)
    k = k.translate(transpose)
    return k.strip()


def store_csv(df, csv_name: str=None, index=None,
              index_label="index"):
    """
    If `index` is not set, it means to True.
    :param df: Dataframe to export as CSV
    :param csv_name: Name of resulting CSV file
    :param index: store index in CSV file
    :return: None
    """
    csv_name = csv_name.strip()
    # if re.match("r^.+?\.csv$", csv_name, flags=re.I) is None:
    #     dot = "" if re.match("r^.+?\.$", csv_name, flags=re.I) is None else "."
    #     csv_name += csv_name + dot + ".csv"
    if index is None:
        index = True
    df.to_csv(csv_name, sep='\t', na_rep='', float_format=None, columns=None, header=True, index=index, 
           index_label=index_label, mode='w', encoding=None, compression='infer', 
           quoting=csv.QUOTE_NONNUMERIC, quotechar='"', line_terminator='\n',
           chunksize=None, date_format=None, doublequote=True, escapechar=None,
           decimal='.')


# будинки квартири
office_types_re_str = r"(б(?:уд)?\.|кв\.|оф(\.|іс)|((адмін\.|адміністративний)\s+)?корп\.|каб\.)"
# вулиці, площі
str_types_re_str = r"(ВУЛ(?:\.?|ИЦЯ)|ПРОСП(\.|ЕКТ)|ПР-Т|ПР\.|ПРОВ(?:\.|УЛОК)|БУЛЬВАР|Б-Р|"\
    r"ПЛОЩА|ПЛ\.|УЗВІЗ|НАБ(?:\.?|ЕРЕЖНА)|ПРОЇЗД|ДОРОГА|ШЛЯХ|АЛЕЯ|СПУСК"\
    r"|КВ(?:\.|АРТАЛ)|МІКРОРАЙОН|МКР-Н|МКРН|МКР Р-Н|\d+\s?КМ)"
# Вахрушеве-666
np_digit_re = "^.+?[\s-]\d+$"
# загальна ідентифікація району
raj_re = "^(?<!М\.).+?ИЙ(?: Р-Н)?$"
# загальна ідентифікація міста
city_start_re = "^М\.\s+"
# ідентифікація помилкового району
# raj_wrong_end_re = re.compile("^.+?(СКИЙ(?: Р-Н)?)$", flags=re.I)
# розділові знаки в кінці рядка
trailing_comma_re = "[-,.\s]+"

obl_marks = {"ВІННИЦЬКОЇ": "ВІННИЦЬКА",
             "ВОЛИНСЬКОЇ": "ВОЛИНСЬКА",
             "ДНІПРОПЕТРОВСЬКОЇ": "ДНІПРОПЕТРОВСЬКА",
             "ДОНЕЦЬКОЇ": "ДОНЕЦЬКА",
             "ЖИТОМИРСЬКОЇ": "ЖИТОМИРСЬКА",
             "ЗАКАРПАТСЬКОЇ": "ЗАКАРПАТСЬКА",
             "ЗАПОРІЗЬКОЇ": "ЗАПОРІЗЬКА",
             "ІВАНО-ФРАНКІВСЬКОЇ": "ІВАНО-ФРАНКІВСЬКА",
             "КИЇВСЬКОЇ": "КИЇВСЬКА",
             "КІРОВОГРАДСЬКОЇ": "КІРОВОГРАДСЬКА",
             "ЛУГАНСЬКОЇ": "ЛУГАНСЬКА",
             "ЛЬВІВСЬКОЇ": "ЛЬВІВСЬКА",
             "ЛЬВІВСЬКА": "ЛЬВІВСЬКА",
             "МИКОЛАЇВСЬКОЇ": "МИКОЛАЇВСЬКА",
             "ОДЕСЬКОЇ": "ОДЕСЬКА",
             "ПОЛТАВСЬКОЇ": "ПОЛТАВСЬКА",
             "РІВНЕНСЬКОЇ": "РІВНЕНСЬКА",
             "СУМСЬКОЇ": "СУМСЬКА",
             "ТЕРНОПІЛЬСЬКОЇ": "ТЕРНОПІЛЬСЬКА",
             "ХАРКІВСЬКОЇ": "ХАРКІВСЬКА",
             "ХЕРСОНСЬКОЇ": "ХЕРСОНСЬКА",
             "ХМЕЛЬНИЦЬКОЇ": "ХМЕЛЬНИЦЬКА",
             "ЧЕРКАСЬКОЇ": "ЧЕРКАСЬКА",
             "ЧЕРНІВЕЦЬКОЇ": "ЧЕРНІВЕЦЬКА",
             "ЧЕРНІГІВСЬКОЇ": "ЧЕРНІГІВСЬКА",
             "АВТОНОМНОЇ РЕСПУБЛІКИ КРИМ": "АВТОНОМНА РЕСПУБЛІКА КРИМ",
             "АР КРИМ": "АВТОНОМНА РЕСПУБЛІКА КРИМ",
             "СЕВАСТОПОЛЯ": "СЕВАСТОПОЛЬ",
             "КИЄВА": "КИЇВ"
             }

obl_marks2 = {
    "АРК": "АВТОНОМНА РЕСПУБЛІКА КРИМ",
    "АРКРИМ": "АВТОНОМНА РЕСПУБЛІКА КРИМ",
    "АНД": "АМУР-НИЖНЬОДНІПРОВСЬКИЙ",
    "Ц-МІСЬКИЙ": "ЦЕНТРАЛЬНО-МІСЬКИЙ",
}

# області
oblasts = "|".join(
    [o for o in obl_marks.values() if o not in (
        "КИЇВ", "СЕВАСТОПОЛЬ", "АВТОНОМНА РЕСПУБЛІКА КРИМ")])
# області та міста спецстатусу
oblasts_v3 = r"\b((?:М\. )?(?:КИЇВ|СЕВАСТОПОЛЬ)|(?:" + oblasts + r")(?:\s+ОБЛ\.?)?|АВТОНОМНА РЕСПУБЛІКА КРИМ)(?!-)\b"

house_parts = [
    "ВУЛ(?:\.?|ИЦЯ)", "ПЛОЩА", "ПЛ\.",  "НАБ(?:\.?|ЕРЕЖНА)", "ДОРОГА",
    "АЛЕЯ"
]

cities = {
    "М. СІМФЕРОПОЛЬ": "АВТОНОМНА РЕСПУБЛІКА КРИМ",
    "М. ВІННИЦЯ": "ВІННИЦЬКА",
    "М. ЛУЦЬК": "ВОЛИНСЬКА",
    "М. ДНІПРО": "ДНІПРОПЕТРОВСЬКА",
    "М. ДНІПРОПЕТРОВСЬК": "ДНІПРОПЕТРОВСЬКА",
    "М. ДОНЕЦЬК": "ДОНЕЦЬКА",
    "М. ЖИТОМИР": "ЖИТОМИРСЬКА",
    "М. УЖГОРОД": "ЗАКАРПАТСЬКА",
    "М. ЗАПОРІЖЖЯ": "ЗАПОРІЗЬКА",
    "М. ІВАНО-ФРАНКІВСЬК": "ІВАНО-ФРАНКІВСЬКА",
    "М. КИЇВ": "КИЇВСЬКА",
    "М. КРОПИВНИЦЬКИЙ": "КІРОВОГРАДСЬКА",
    "М. ЛУГАНСЬК": "ЛУГАНСЬКА",
    "М. ЛЬВІВ": "ЛЬВІВСЬКА",
    "М. МИКОЛАЇВ": "МИКОЛАЇВСЬКА",
    "М. ОДЕСА": "ОДЕСЬКА",
    "М. ПОЛТАВА": "ПОЛТАВСЬКА",
    "М. РІВНЕ": "РІВНЕНСЬКА",
    "М. СУМИ": "СУМСЬКА",
    "М. ТЕРНОПІЛЬ": "ТЕРНОПІЛЬСЬКА",
    "М. ХАРКІВ": "ХАРКІВСЬКА",
    "М. ХЕРСОН": "ХЕРСОНСЬКА",
    "М. ХМЕЛЬНИЦЬКИЙ": "ХМЕЛЬНИЦЬКА",
    "М. ЧЕРКАСИ": "ЧЕРКАСЬКА",
    "М. ЧЕРНІВЦІ": "ЧЕРНІВЕЦЬКА",
    "М. ЧЕРНІГІВ": "ЧЕРНІГІВСЬКА"}

marks = {'УКРАЇНА': '',
         'МІСТО': 'М.',
         'СЕЛО': 'С.',
         r'ПОС.': 'С-ЩЕ ',
         r'СЕЛ\.\s?': 'С-ЩЕ ',
         r'С-ЩЕ[\s\.]+': 'С-ЩЕ ',
         r'ОБЛ(?!\.)': 'ОБЛ.',
         'ОБЛАСТЬ': 'ОБЛ.',
         'МІКРОРАЙОНУ?': 'МКРН.',
         "МІКРО\s?РАЙОН":  'МКРН.',
         'РАЙОНУ': 'Р-Н',
         'РАЙОН': 'Р-Н',
         'СЕЛИЩЕ МІСЬКОГО ТИПУ': 'СМТ',
         'СЕЛИЩЕ': 'С-ЩЕ ',
         r'СМТ\.': 'СМТ ',
         r"С\.?(\s+)?М\.?(\s+)?Т\.?(\s+)?": 'СМТ ',
         r"П\.": "С.",
         'БУДИНОК': 'БУД.',
         'КОРПУС': 'КОРП.',
         'КВАРТИРА': 'КВ.',
         'КІМНАТА': 'К.',
         'ПЛОЩА': 'ПЛ.',
         'БУЛЬВАР': 'Б-Р.',
         'ПРОСПЕКТ': 'ПРОСП.',
         'Р-НУ': 'Р-Н',
         'Р-ОН': 'Р-Н',
         "ОБЛАСТІ": 'ОБЛ.',
         "ВУЛИЦЯ": "ВУЛ. ",
         "ВУЛ(\.|\b)": "ВУЛ. "
         }