#!/usr/bin/env python
# -*- coding: utf-8 -*-


double_cities = [
    "БІЛГОРОД-ДНІСТРОВСЬКИЙ", "ВОЛОДИМИР-ВОЛИНСЬКИЙ", "КАМ’ЯНЕЦЬ-ПОДІЛЬСЬКИЙ",
    "КАМІНЬ-КАШИРСЬКИЙ", "КОРСУНЬ-ШЕВЧЕНКІВСЬКИЙ", "КРОПИВНИЦЬКИЙ", "МОГИЛІВ-ПОДІЛЬСЬКИЙ",
    "НОВГОРОД-СІВЕРСЬКИЙ", "НОВОГРАД-ВОЛИНСЬКИЙ", "ПЕРВОМАЙСЬКИЙ", "ПЕРЕЯСЛАВ-ХМЕЛЬНИЦЬКИЙ",
    "ХМЕЛЬНИЦЬКИЙ", "КІРОВОГРАДСЬКИЙ"
]

oblasts_has_raion_cities = [
    "КИЇВ", "СЕВАСТОПОЛЬ", "АВТОНОМНА РЕСПУБЛІКА КРИМ", "ВІННИЦЬКА", "ДНІПРОПЕТРОВСЬКА", "ДОНЕЦЬКА",
    "ЖИТОМИРСЬКА", "ЗАПОРІЗЬКА", "КІРОВОГРАДСЬКА", "ЛУГАНСЬКА", "ЛЬВІВСЬКА", "М. КИЇВ", "М. СЕВАСТОПОЛЬ",
    "МИКОЛАЇВСЬКА", "ОДЕСЬКА", "ПОЛТАВСЬКА", "СУМСЬКА", "ХАРКІВСЬКА", "ХЕРСОНСЬКА", "ЧЕРКАСЬКА", "ЧЕРНІВЕЦЬКА",
    "ЧЕРНІГІВСЬКА"]

rajons_oblast = {
    "АВТОНОМНА РЕСПУБЛІКА КРИМ": [
        "БАХЧИСАРАЙСЬКИЙ",
        "БІЛОГІРСЬКИЙ",
        "ДЖАНКОЙСЬКИЙ",
        "КРАСНОГВАРДІЙСЬКИЙ",
        "КРАСНОПЕРЕКОПСЬКИЙ",
        "КІРОВСЬКИЙ",
        "ЛЕНІНСЬКИЙ",
        "НИЖНЬОГІРСЬКИЙ",
        "ПЕРВОМАЙСЬКИЙ",
        "РОЗДОЛЬНЕНСЬКИЙ",
        "САКСЬКИЙ",
        "СОВЄТСЬКИЙ",
        "СІМФЕРОПОЛЬСЬКИЙ",
        "ЧОРНОМОРСЬКИЙ"
    ],
    "ВОЛИНСЬКА": [
        "ВОЛОДИМИР-ВОЛИНСЬКИЙ",
        "ГОРОХІВСЬКИЙ",
        "КАМІНЬ-КАШИРСЬКИЙ",
        "КОВЕЛЬСЬКИЙ",
        "КІВЕРЦІВСЬКИЙ",
        "ЛОКАЧИНСЬКИЙ",
        "ЛУЦЬКИЙ",
        "ЛЮБЕШІВСЬКИЙ",
        "ЛЮБОМЛЬСЬКИЙ",
        "МАНЕВИЦЬКИЙ",
        "РАТНІВСЬКИЙ",
        "РОЖИЩЕНСЬКИЙ",
        "СТАРОВИЖІВСЬКИЙ",
        "ТУРІЙСЬКИЙ",
        "ШАЦЬКИЙ",
        "ІВАНИЧІВСЬКИЙ"
    ],
    "ВІННИЦЬКА": [
        "БАРСЬКИЙ",
        "БЕРШАДСЬКИЙ",
        "ВІННИЦЬКИЙ",
        "ГАЙСИНСЬКИЙ",
        "ЖМЕРИНСЬКИЙ",
        "КАЛИНІВСЬКИЙ",
        "КОЗЯТИНСЬКИЙ",
        "КРИЖОПІЛЬСЬКИЙ",
        "ЛИПОВЕЦЬКИЙ",
        "ЛІТИНСЬКИЙ",
        "МОГИЛІВ-ПОДІЛЬСЬКИЙ",
        "МУРОВАНОКУРИЛОВЕЦЬКИЙ",
        "НЕМИРІВСЬКИЙ",
        "ОРАТІВСЬКИЙ",
        "ПОГРЕБИЩЕНСЬКИЙ",
        "ПІЩАНСЬКИЙ",
        "ТЕПЛИЦЬКИЙ",
        "ТИВРІВСЬКИЙ",
        "ТОМАШПІЛЬСЬКИЙ",
        "ТРОСТЯНЕЦЬКИЙ",
        "ТУЛЬЧИНСЬКИЙ",
        "ХМІЛЬНИЦЬКИЙ",
        "ЧЕРНІВЕЦЬКИЙ",
        "ЧЕЧЕЛЬНИЦЬКИЙ",
        "ШАРГОРОДСЬКИЙ",
        "ЯМПІЛЬСЬКИЙ",
        "ІЛЛІНЕЦЬКИЙ"
    ],
    "ДНІПРОПЕТРОВСЬКА": [
        "АПОСТОЛІВСЬКИЙ",
        "ВАСИЛЬКІВСЬКИЙ",
        "ВЕРХНЬОДНІПРОВСЬКИЙ",
        "ДНІПРОВСЬКИЙ",
        "ДНІПРОПЕТРОВСЬКИЙ",
        "КРИВОРІЗЬКИЙ",
        "КРИНИЧАНСЬКИЙ",
        "МАГДАЛИНІВСЬКИЙ",
        "МЕЖІВСЬКИЙ",
        "НОВОМОСКОВСЬКИЙ",
        "НІКОПОЛЬСЬКИЙ",
        "П’ЯТИХАТСЬКИЙ",
        "ПАВЛОГРАДСЬКИЙ",
        "ПЕТРИКІВСЬКИЙ",
        "ПЕТРОПАВЛІВСЬКИЙ",
        "ПОКРОВСЬКИЙ",
        "СИНЕЛЬНИКІВСЬКИЙ",
        "СОЛОНЯНСЬКИЙ",
        "СОФІЇВСЬКИЙ",
        "ТОМАКІВСЬКИЙ",
        "ЦАРИЧАНСЬКИЙ",
        "ШИРОКІВСЬКИЙ",
        "ЮР’ЇВСЬКИЙ"
    ],
    "ДОНЕЦЬКА": [
        "АМВРОСІЇВСЬКИЙ",
        "БАХМУТСЬКИЙ",
        "АРТЕМІВСЬКИЙ",
        "БОЙКІВСЬКИЙ",
        "ТЕЛЬМАНІВСЬКИЙ",
        "ВЕЛИКОНОВОСІЛКІВСЬКИЙ",
        "ВОЛНОВАСЬКИЙ",
        "ДОБРОПІЛЬСЬКИЙ",
        "КОСТЯНТИНІВСЬКИЙ",
        "ЛИМАНСЬКИЙ",
        "КРАСНОЛИМАНСЬКИЙ",
        "МАНГУШСЬКИЙ",
        "ПЕРШОТРАВНЕВИЙ",
        "МАР’ЇНСЬКИЙ",
        "НОВОАЗОВСЬКИЙ",
        "НІКОЛЬСЬКИЙ",
        "ВОЛОДАРСЬКИЙ",
        "ОЛЕКСАНДРІВСЬКИЙ",
        "ПОКРОВСЬКИЙ",
        "КРАСНОАРМІЙСЬКИЙ",
        "СЛОВ’ЯНСЬКИЙ",
        "СТАРОБЕШІВСЬКИЙ",
        "ШАХТАРСЬКИЙ",
        "ЯСИНУВАТСЬКИЙ"
    ],
    "ЖИТОМИРСЬКА": [
        "АНДРУШІВСЬКИЙ",
        "БАРАНІВСЬКИЙ",
        "БЕРДИЧІВСЬКИЙ",
        "БРУСИЛІВСЬКИЙ",
        "ЖИТОМИРСЬКИЙ",
        "КОРОСТЕНСЬКИЙ",
        "КОРОСТИШІВСЬКИЙ",
        "ЛУГИНСЬКИЙ",
        "ЛЮБАРСЬКИЙ",
        "МАЛИНСЬКИЙ",
        "НАРОДИЦЬКИЙ",
        "НОВОГРАД-ВОЛИНСЬКИЙ",
        "ОВРУЦЬКИЙ",
        "ОЛЕВСЬКИЙ",
        "ПОПІЛЬНЯНСЬКИЙ",
        "ПУЛИНСЬКИЙ",
        "ЧЕРВОНОАРМІЙСЬКИЙ",
        "РАДОМИШЛЬСЬКИЙ",
        "РОМАНІВСЬКИЙ",
        "РУЖИНСЬКИЙ",
        "ХОРОШІВСЬКИЙ",
        "ВОЛОДАРСЬКО-ВОЛИНСЬКИЙ",
        "ЧЕРНЯХІВСЬКИЙ",
        "ЧУДНІВСЬКИЙ",
        "ЄМІЛЬЧИНСЬКИЙ"
    ],
    "ЗАКАРПАТСЬКА": [
        "БЕРЕГІВСЬКИЙ",
        "ВЕЛИКОБЕРЕЗНЯНСЬКИЙ",
        "ВИНОГРАДІВСЬКИЙ",
        "ВОЛОВЕЦЬКИЙ",
        "МУКАЧІВСЬКИЙ",
        "МІЖГІРСЬКИЙ",
        "ПЕРЕЧИНСЬКИЙ",
        "РАХІВСЬКИЙ",
        "СВАЛЯВСЬКИЙ",
        "ТЯЧІВСЬКИЙ",
        "УЖГОРОДСЬКИЙ",
        "ХУСТСЬКИЙ",
        "ІРШАВСЬКИЙ"
    ],
    "ЗАПОРІЗЬКА": [
        "БЕРДЯНСЬКИЙ",
        "БІЛЬМАЦЬКИЙ",
        "КУЙБИШЕВСЬКИЙ",
        "ВАСИЛІВСЬКИЙ",
        "ВЕЛИКОБІЛОЗЕРСЬКИЙ",
        "ВЕСЕЛІВСЬКИЙ",
        "ВІЛЬНЯНСЬКИЙ",
        "ГУЛЯЙПІЛЬСЬКИЙ",
        "ЗАПОРІЗЬКИЙ",
        "КАМ’ЯНСЬКО-ДНІПРОВСЬКИЙ",
        "МЕЛІТОПОЛЬСЬКИЙ",
        "МИХАЙЛІВСЬКИЙ",
        "НОВОМИКОЛАЇВСЬКИЙ",
        "ОРІХІВСЬКИЙ",
        "ПОЛОГІВСЬКИЙ",
        "ПРИАЗОВСЬКИЙ",
        "ПРИМОРСЬКИЙ",
        "РОЗІВСЬКИЙ",
        "ТОКМАЦЬКИЙ",
        "ЧЕРНІГІВСЬКИЙ",
        "ЯКИМІВСЬКИЙ"
    ],
    "КИЇВСЬКА": [
        "БАРИШІВСЬКИЙ",
        "БОГУСЛАВСЬКИЙ",
        "БОРИСПІЛЬСЬКИЙ",
        "БОРОДЯНСЬКИЙ",
        "БРОВАРСЬКИЙ",
        "БІЛОЦЕРКІВСЬКИЙ",
        "ВАСИЛЬКІВСЬКИЙ",
        "ВИШГОРОДСЬКИЙ",
        "ВОЛОДАРСЬКИЙ",
        "ЗГУРІВСЬКИЙ",
        "КАГАРЛИЦЬКИЙ",
        "КИЄВО-СВЯТОШИНСЬКИЙ",
        "МАКАРІВСЬКИЙ",
        "МИРОНІВСЬКИЙ",
        "ОБУХІВСЬКИЙ",
        "ПЕРЕЯСЛАВ-ХМЕЛЬНИЦЬКИЙ",
        "ПОЛІСЬКИЙ",
        "РОКИТНЯНСЬКИЙ",
        "СКВИРСЬКИЙ",
        "СТАВИЩЕНСЬКИЙ",
        "ТАРАЩАНСЬКИЙ",
        "ТЕТІЇВСЬКИЙ",
        "ФАСТІВСЬКИЙ",
        "ЯГОТИНСЬКИЙ",
        "ІВАНКІВСЬКИЙ"
    ],
    "КІРОВОГРАДСЬКА": [
        "БЛАГОВІЩЕНСЬКИЙ",
        "УЛЬЯНОВСЬКИЙ",
        "БОБРИНЕЦЬКИЙ",
        "ВІЛЬШАНСЬКИЙ",
        "ГАЙВОРОНСЬКИЙ",
        "ГОЛОВАНІВСЬКИЙ",
        "ДОБРОВЕЛИЧКІВСЬКИЙ",
        "ДОЛИНСЬКИЙ",
        "ЗНАМ’ЯНСЬКИЙ",
        "КОМПАНІЇВСЬКИЙ",
        "КРОПИВНИЦЬКИЙ",
        "КІРОВОГРАДСЬКИЙ",
        "МАЛОВИСКІВСЬКИЙ",
        "НОВГОРОДКІВСЬКИЙ",
        "НОВОАРХАНГЕЛЬСЬКИЙ",
        "НОВОМИРГОРОДСЬКИЙ",
        "НОВОУКРАЇНСЬКИЙ",
        "ОЛЕКСАНДРІВСЬКИЙ",
        "ОЛЕКСАНДРІЙСЬКИЙ",
        "ОНУФРІЇВСЬКИЙ",
        "ПЕТРІВСЬКИЙ",
        "СВІТЛОВОДСЬКИЙ",
        "УСТИНІВСЬКИЙ"
    ],
    "ЛУГАНСЬКА": [
        "АНТРАЦИТІВСЬКИЙ",
        "БІЛОВОДСЬКИЙ",
        "БІЛОКУРАКИНСЬКИЙ",
        "ДОВЖАНСЬКИЙ",
        "СВЕРДЛОВСЬКИЙ",
        "КРЕМІНСЬКИЙ",
        "ЛУТУГИНСЬКИЙ",
        "МАРКІВСЬКИЙ",
        "МІЛОВСЬКИЙ",
        "НОВОАЙДАРСЬКИЙ",
        "НОВОПСКОВСЬКИЙ",
        "ПЕРЕВАЛЬСЬКИЙ",
        "ПОПАСНЯНСЬКИЙ",
        "СВАТІВСЬКИЙ",
        "СЛОВ’ЯНОСЕРБСЬКИЙ",
        "СОРОКИНСЬКИЙ",
        "КРАСНОДОНСЬКИЙ",
        "СТАНИЧНО-ЛУГАНСЬКИЙ",
        "СТАРОБІЛЬСЬКИЙ",
        "ТРОЇЦЬКИЙ"
    ],
    "ЛЬВІВСЬКА": [
        "БРОДІВСЬКИЙ",
        "БУСЬКИЙ",
        "ГОРОДОЦЬКИЙ",
        "ДРОГОБИЦЬКИЙ",
        "ЖИДАЧІВСЬКИЙ",
        "ЖОВКІВСЬКИЙ",
        "ЗОЛОЧІВСЬКИЙ",
        "КАМ’ЯНКА-БУЗЬКИЙ",
        "МИКОЛАЇВСЬКИЙ",
        "МОСТИСЬКИЙ",
        "ПЕРЕМИШЛЯНСЬКИЙ",
        "ПУСТОМИТІВСЬКИЙ",
        "РАДЕХІВСЬКИЙ",
        "САМБІРСЬКИЙ",
        "СКОЛІВСЬКИЙ",
        "СОКАЛЬСЬКИЙ",
        "СТАРОСАМБІРСЬКИЙ",
        "СТРИЙСЬКИЙ",
        "ТУРКІВСЬКИЙ",
        "ЯВОРІВСЬКИЙ"
    ],
    "МИКОЛАЇВСЬКА": [
        "АРБУЗИНСЬКИЙ",
        "БАШТАНСЬКИЙ",
        "БЕРЕЗАНСЬКИЙ",
        "БЕРЕЗНЕГУВАТСЬКИЙ",
        "БРАТСЬКИЙ",
        "ВЕСЕЛИНІВСЬКИЙ",
        "ВОЗНЕСЕНСЬКИЙ",
        "ВРАДІЇВСЬКИЙ",
        "ВІТОВСЬКИЙ",
        "ЖОВТНЕВИЙ",
        "ДОМАНІВСЬКИЙ",
        "КАЗАНКІВСЬКИЙ",
        "КРИВООЗЕРСЬКИЙ",
        "МИКОЛАЇВСЬКИЙ",
        "НОВОБУЗЬКИЙ",
        "НОВООДЕСЬКИЙ",
        "ОЧАКІВСЬКИЙ",
        "ПЕРВОМАЙСЬКИЙ",
        "СНІГУРІВСЬКИЙ",
        "ЄЛАНЕЦЬКИЙ"
    ],
    "ОДЕСЬКА": [
        "АНАНЬЇВСЬКИЙ",
        "АРЦИЗЬКИЙ",
        "БАЛТСЬКИЙ",
        "БЕРЕЗІВСЬКИЙ",
        "БОЛГРАДСЬКИЙ",
        "БІЛГОРОД-ДНІСТРОВСЬКИЙ",
        "БІЛЯЇВСЬКИЙ",
        "ВЕЛИКОМИХАЙЛІВСЬКИЙ",
        "ЗАХАРІВСЬКИЙ",
        "ФРУНЗІВСЬКИЙ",
        "КОДИМСЬКИЙ",
        "КІЛІЙСЬКИЙ",
        "ЛИМАНСЬКИЙ",
        "КОМІНТЕРНІВСЬКИЙ",
        "ЛЮБАШІВСЬКИЙ",
        "МИКОЛАЇВСЬКИЙ",
        "ОВІДІОПОЛЬСЬКИЙ",
        "ОКНЯНСЬКИЙ",
        "КРАСНООКНЯНСЬКИЙ",
        "ПОДІЛЬСЬКИЙ",
        "КОТОВСЬКИЙ",
        "РЕНІЙСЬКИЙ",
        "РОЗДІЛЬНЯНСЬКИЙ",
        "САВРАНСЬКИЙ",
        "САРАТСЬКИЙ",
        "ТАРУТИНСЬКИЙ",
        "ТАТАРБУНАРСЬКИЙ",
        "ШИРЯЇВСЬКИЙ",
        "ІВАНІВСЬКИЙ",
        "ІЗМАЇЛЬСЬКИЙ"
    ],
    "ПОЛТАВСЬКА": [
        "ВЕЛИКОБАГАЧАНСЬКИЙ",
        "ГАДЯЦЬКИЙ",
        "ГЛОБИНСЬКИЙ",
        "ГРЕБІНКІВСЬКИЙ",
        "ДИКАНСЬКИЙ",
        "ЗІНЬКІВСЬКИЙ",
        "КАРЛІВСЬКИЙ",
        "КОБЕЛЯЦЬКИЙ",
        "КОЗЕЛЬЩИНСЬКИЙ",
        "КОТЕЛЕВСЬКИЙ",
        "КРЕМЕНЧУЦЬКИЙ",
        "ЛОХВИЦЬКИЙ",
        "ЛУБЕНСЬКИЙ",
        "МАШІВСЬКИЙ",
        "МИРГОРОДСЬКИЙ",
        "НОВОСАНЖАРСЬКИЙ",
        "ОРЖИЦЬКИЙ",
        "ПИРЯТИНСЬКИЙ",
        "ПОЛТАВСЬКИЙ",
        "РЕШЕТИЛІВСЬКИЙ",
        "СЕМЕНІВСЬКИЙ",
        "ХОРОЛЬСЬКИЙ",
        "ЧОРНУХИНСЬКИЙ",
        "ЧУТІВСЬКИЙ",
        "ШИШАЦЬКИЙ"
    ],
    "РІВНЕНСЬКА": [
        "БЕРЕЗНІВСЬКИЙ",
        "ВОЛОДИМИРЕЦЬКИЙ",
        "ГОЩАНСЬКИЙ",
        "ДЕМИДІВСЬКИЙ",
        "ДУБЕНСЬКИЙ",
        "ДУБРОВИЦЬКИЙ",
        "ЗАРІЧНЕНСЬКИЙ",
        "ЗДОЛБУНІВСЬКИЙ",
        "КОРЕЦЬКИЙ",
        "КОСТОПІЛЬСЬКИЙ",
        "МЛИНІВСЬКИЙ",
        "ОСТРОЗЬКИЙ",
        "РАДИВИЛІВСЬКИЙ",
        "РОКИТНІВСЬКИЙ",
        "РІВНЕНСЬКИЙ",
        "САРНЕНСЬКИЙ"
    ],
    "СУМСЬКА": [
        "БУРИНСЬКИЙ",
        "БІЛОПІЛЬСЬКИЙ",
        "ВЕЛИКОПИСАРІВСЬКИЙ",
        "ГЛУХІВСЬКИЙ",
        "КОНОТОПСЬКИЙ",
        "КРАСНОПІЛЬСЬКИЙ",
        "КРОЛЕВЕЦЬКИЙ",
        "ЛЕБЕДИНСЬКИЙ",
        "ЛИПОВОДОЛИНСЬКИЙ",
        "НЕДРИГАЙЛІВСЬКИЙ",
        "ОХТИРСЬКИЙ",
        "ПУТИВЛЬСЬКИЙ",
        "РОМЕНСЬКИЙ",
        "СЕРЕДИНО-БУДСЬКИЙ",
        "СУМСЬКИЙ",
        "ТРОСТЯНЕЦЬКИЙ",
        "ШОСТКИНСЬКИЙ",
        "ЯМПІЛЬСЬКИЙ"
    ],
    "ТЕРНОПІЛЬСЬКА": [
        "БЕРЕЖАНСЬКИЙ",
        "БОРЩІВСЬКИЙ",
        "БУЧАЦЬКИЙ",
        "ГУСЯТИНСЬКИЙ",
        "ЗАЛІЩИЦЬКИЙ",
        "ЗБАРАЗЬКИЙ",
        "ЗБОРІВСЬКИЙ",
        "КОЗІВСЬКИЙ",
        "КРЕМЕНЕЦЬКИЙ",
        "ЛАНОВЕЦЬКИЙ",
        "МОНАСТИРИСЬКИЙ",
        "ПІДВОЛОЧИСЬКИЙ",
        "ПІДГАЄЦЬКИЙ",
        "ТЕРЕБОВЛЯНСЬКИЙ",
        "ТЕРНОПІЛЬСЬКИЙ",
        "ЧОРТКІВСЬКИЙ",
        "ШУМСЬКИЙ"
    ],
    "ХАРКІВСЬКА": [
        "БАЛАКЛІЙСЬКИЙ",
        "БАРВІНКІВСЬКИЙ",
        "БЛИЗНЮКІВСЬКИЙ",
        "БОГОДУХІВСЬКИЙ",
        "БОРІВСЬКИЙ",
        "ВАЛКІВСЬКИЙ",
        "ВЕЛИКОБУРЛУЦЬКИЙ",
        "ВОВЧАНСЬКИЙ",
        "ДВОРІЧАНСЬКИЙ",
        "ДЕРГАЧІВСЬКИЙ",
        "ЗАЧЕПИЛІВСЬКИЙ",
        "ЗМІЇВСЬКИЙ",
        "ЗОЛОЧІВСЬКИЙ",
        "КЕГИЧІВСЬКИЙ",
        "КОЛОМАЦЬКИЙ",
        "КРАСНОГРАДСЬКИЙ",
        "КРАСНОКУТСЬКИЙ",
        "КУП’ЯНСЬКИЙ",
        "ЛОЗІВСЬКИЙ",
        "НОВОВОДОЛАЗЬКИЙ",
        "ПЕРВОМАЙСЬКИЙ",
        "ПЕЧЕНІЗЬКИЙ",
        "САХНОВЩИНСЬКИЙ",
        "ХАРКІВСЬКИЙ",
        "ЧУГУЇВСЬКИЙ",
        "ШЕВЧЕНКІВСЬКИЙ",
        "ІЗЮМСЬКИЙ"
    ],
    "ХЕРСОНСЬКА": [
        "БЕРИСЛАВСЬКИЙ",
        "БІЛОЗЕРСЬКИЙ",
        "ВЕЛИКОЛЕПЕТИСЬКИЙ",
        "ВЕЛИКООЛЕКСАНДРІВСЬКИЙ",
        "ВЕРХНЬОРОГАЧИЦЬКИЙ",
        "ВИСОКОПІЛЬСЬКИЙ",
        "ГЕНІЧЕСЬКИЙ",
        "ГОЛОПРИСТАНСЬКИЙ",
        "ГОРНОСТАЇВСЬКИЙ",
        "КАЛАНЧАЦЬКИЙ",
        "КАХОВСЬКИЙ",
        "НИЖНЬОСІРОГОЗЬКИЙ",
        "НОВОВОРОНЦОВСЬКИЙ",
        "НОВОТРОЇЦЬКИЙ",
        "ОЛЕШКІВСЬКИЙ",
        "ЦЮРУПИНСЬКИЙ",
        "СКАДОВСЬКИЙ",
        "ЧАПЛИНСЬКИЙ",
        "ІВАНІВСЬКИЙ"
    ],
    "ХМЕЛЬНИЦЬКА": [
        "БІЛОГІРСЬКИЙ",
        "ВОЛОЧИСЬКИЙ",
        "ВІНЬКОВЕЦЬКИЙ",
        "ГОРОДОЦЬКИЙ",
        "ДЕРАЖНЯНСЬКИЙ",
        "ДУНАЄВЕЦЬКИЙ",
        "КАМ’ЯНЕЦЬ-ПОДІЛЬСЬКИЙ",
        "КРАСИЛІВСЬКИЙ",
        "ЛЕТИЧІВСЬКИЙ",
        "НОВОУШИЦЬКИЙ",
        "ПОЛОНСЬКИЙ",
        "СЛАВУТСЬКИЙ",
        "СТАРОКОСТЯНТИНІВСЬКИЙ",
        "СТАРОСИНЯВСЬКИЙ",
        "ТЕОФІПОЛЬСЬКИЙ",
        "ХМЕЛЬНИЦЬКИЙ",
        "ЧЕМЕРОВЕЦЬКИЙ",
        "ШЕПЕТІВСЬКИЙ",
        "ЯРМОЛИНЕЦЬКИЙ",
        "ІЗЯСЛАВСЬКИЙ"
    ],
    "ЧЕРКАСЬКА": [
        "ГОРОДИЩЕНСЬКИЙ",
        "ДРАБІВСЬКИЙ",
        "ЖАШКІВСЬКИЙ",
        "ЗВЕНИГОРОДСЬКИЙ",
        "ЗОЛОТОНІСЬКИЙ",
        "КАМ’ЯНСЬКИЙ",
        "КАНІВСЬКИЙ",
        "КАТЕРИНОПІЛЬСЬКИЙ",
        "КОРСУНЬ-ШЕВЧЕНКІВСЬКИЙ",
        "ЛИСЯНСЬКИЙ",
        "МАНЬКІВСЬКИЙ",
        "МОНАСТИРИЩЕНСЬКИЙ",
        "СМІЛЯНСЬКИЙ",
        "ТАЛЬНІВСЬКИЙ",
        "УМАНСЬКИЙ",
        "ХРИСТИНІВСЬКИЙ",
        "ЧЕРКАСЬКИЙ",
        "ЧИГИРИНСЬКИЙ",
        "ЧОРНОБАЇВСЬКИЙ",
        "ШПОЛЯНСЬКИЙ"
    ],
    "ЧЕРНІВЕЦЬКА": [
        "ВИЖНИЦЬКИЙ",
        "ГЕРЦАЇВСЬКИЙ",
        "ГЛИБОЦЬКИЙ",
        "ЗАСТАВНІВСЬКИЙ",
        "КЕЛЬМЕНЕЦЬКИЙ",
        "КІЦМАНСЬКИЙ",
        "НОВОСЕЛИЦЬКИЙ",
        "ПУТИЛЬСЬКИЙ",
        "СОКИРЯНСЬКИЙ",
        "СТОРОЖИНЕЦЬКИЙ",
        "ХОТИНСЬКИЙ"
    ],
    "ЧЕРНІГІВСЬКА": [
        "БАХМАЦЬКИЙ",
        "БОБРОВИЦЬКИЙ",
        "БОРЗНЯНСЬКИЙ",
        "ВАРВИНСЬКИЙ",
        "ГОРОДНЯНСЬКИЙ",
        "КОЗЕЛЕЦЬКИЙ",
        "КОРОПСЬКИЙ",
        "КОРЮКІВСЬКИЙ",
        "КУЛИКІВСЬКИЙ",
        "МЕНСЬКИЙ",
        "НОВГОРОД-СІВЕРСЬКИЙ",
        "НОСІВСЬКИЙ",
        "НІЖИНСЬКИЙ",
        "ПРИЛУЦЬКИЙ",
        "РІПКИНСЬКИЙ",
        "СЕМЕНІВСЬКИЙ",
        "СНОВСЬКИЙ",
        "ЩОРСЬКИЙ",
        "СОСНИЦЬКИЙ",
        "СРІБНЯНСЬКИЙ",
        "ТАЛАЛАЇВСЬКИЙ",
        "ЧЕРНІГІВСЬКИЙ",
        "ІЧНЯНСЬКИЙ"
    ],
    "ІВАНО-ФРАНКІВСЬКА": [
        "БОГОРОДЧАНСЬКИЙ",
        "ВЕРХОВИНСЬКИЙ",
        "ГАЛИЦЬКИЙ",
        "ГОРОДЕНКІВСЬКИЙ",
        "ДОЛИНСЬКИЙ",
        "КАЛУСЬКИЙ",
        "КОЛОМИЙСЬКИЙ",
        "КОСІВСЬКИЙ",
        "НАДВІРНЯНСЬКИЙ",
        "РОГАТИНСЬКИЙ",
        "РОЖНЯТІВСЬКИЙ",
        "СНЯТИНСЬКИЙ",
        "ТИСМЕНИЦЬКИЙ",
        "ТЛУМАЦЬКИЙ"
    ],
    "СЕВАСТОПОЛЬ": [
        "БАЛАКЛАВСЬКИЙ",
        "ГАГАРІНСЬКИЙ",
        "ЛЕНІНСЬКИЙ",
        "НАХІМОВСЬКИЙ"
    ],
    "КИЇВ": [
        "ВАТУТІНСЬКИЙ",
        "ГОЛОСІЇВСЬКИЙ",
        "ДАРНИЦЬКИЙ",
        "ДЕСНЯНСЬКИЙ",
        "ДНІПРОВСЬКИЙ",
        "ЖОВТНЕВИЙ",
        "ЗАЛІЗНИЧНИЙ",
        "ЛЕНІНГРАДСЬКИЙ",
        "МОСКОВСЬКИЙ",
        "МІНСЬКИЙ",
        "ОБОЛОНСЬКИЙ",
        "ПЕЧЕРСЬКИЙ",
        "ПОДІЛЬСЬКИЙ",
        "РАДЯНСЬКИЙ",
        "СВЯТОШИНСЬКИЙ",
        "СОЛОМ’ЯНСЬКИЙ",
        "СТАРОКИЇВСЬКИЙ",
        "ХАРКІВСЬКИЙ",
        "ШЕВЧЕНКІВСЬКИЙ"
    ]
}

city_rajons = {
    "М. СЕВАСТОПОЛЬ": {
        "БАЛАКЛАВСЬКИЙ",
        "ГАГАРІНСЬКИЙ",
        "ЛЕНІНСЬКИЙ",
        "НАХІМОВСЬКИЙ"
    },
    "М. КИЇВ": {
        "ВАТУТІНСЬКИЙ",
        "ГОЛОСІЇВСЬКИЙ",
        "ДАРНИЦЬКИЙ",
        "ДЕСНЯНСЬКИЙ",
        "ДНІПРОВСЬКИЙ",
        "ЖОВТНЕВИЙ",
        "ЗАЛІЗНИЧНИЙ",
        "ЛЕНІНГРАДСЬКИЙ",
        "МОСКОВСЬКИЙ",
        "МІНСЬКИЙ",
        "ОБОЛОНСЬКИЙ",
        "ПЕЧЕРСЬКИЙ",
        "ПОДІЛЬСЬКИЙ",
        "РАДЯНСЬКИЙ",
        "СВЯТОШИНСЬКИЙ",
        "СОЛОМ’ЯНСЬКИЙ",
        "СТАРОКИЇВСЬКИЙ",
        "ХАРКІВСЬКИЙ",
        "ШЕВЧЕНКІВСЬКИЙ"
    },
    "ВІННИЦЬКА": {
        "ЗАМОСТЯНСЬКИЙ": "ВІННИЦЯ",
        "ЛЕНІНСЬКИЙ": "ВІННИЦЯ",
        "СТАРОМІСЬКИЙ": "ВІННИЦЯ",
        "АКАДЕМІЧНИЙ": "ВІННИЦЯ",
    },
    "ДОНЕЦЬКА": {
        "БУДЬОННІВСЬКИЙ": "ДОНЕЦЬК",
        "ВОРОШИЛОВСЬКИЙ": "ДОНЕЦЬК",
        "ГІРНИЦЬКИЙ": "МАКІЇВКА",
        "ЖОВТНЕВИЙ": "МАРІУПОЛЬ",
        "КАЛЬМІУСЬКИЙ": "МАРІУПОЛЬ",
        "КАЛІНІНСЬКИЙ": "ДОНЕЦЬК",
        "КИЇВСЬКИЙ": "ДОНЕЦЬК",
        "КУЙБИШЕВСЬКИЙ": "ДОНЕЦЬК",
        "КІРОВСЬКИЙ": "ДОНЕЦЬК",
        "ЛЕНІНСЬКИЙ": "ДОНЕЦЬК",
        "ЛІВОБЕРЕЖНИЙ": "МАРІУПОЛЬ",
        "МИКИТІВСЬКИЙ": "ГОРЛІВКА",
        "ОРДЖОНІКІДЗЕВСЬКИЙ": "МАРІУПОЛЬ",
        "ПЕТРОВСЬКИЙ": "ДОНЕЦЬК",
        "ПРИМОРСЬКИЙ": "МАРІУПОЛЬ",
        "ПРОЛЕТАРСЬКИЙ": "ДОНЕЦЬК",
        "СОВЄТСЬКИЙ": "МАКІЇВКА",
        "ЦЕНТРАЛЬНИЙ": "МАРІУПОЛЬ",
        "ЦЕНТРАЛЬНО-МІСЬКИЙ": "ГОРЛІВКА",
        "ЧЕРВОНОГВАРДІЙСЬКИЙ": "МАКІЇВКА",
        "ІЛЛІЧІВСЬКИЙ": "МАРІУПОЛЬ"
    },
    "ДНІПРОПЕТРОВСЬКА": {
        "АМУР-НИЖНЬОДНІПРОВСЬКИЙ": "ДНІПРО|ДНІПРОПЕТРОВСЬК",
        "БАБУШКІНСЬКИЙ": "ДНІПРОПЕТРОВСЬК",
        "БАГЛІЙСЬКИЙ": "ДНІПРОДЗЕРЖИНСЬК",
        "ДЗЕРЖИНСЬКИЙ": "КРИВИЙ РІГ",
        "ДНІПРОВСЬКИЙ": "КАМ’ЯНСЬКЕ",
        "ДОВГИНЦІВСЬКИЙ": "КРИВИЙ РІГ",
        "ЖОВТНЕВИЙ": "ДНІПРОПЕТРОВСЬК",
        "ЗАВОДСЬКИЙ": "КАМ’ЯНСЬКЕ",
        "КРАСНОГВАРДІЙСЬКИЙ": "ДНІПРОПЕТРОВСЬК",
        "КІРОВСЬКИЙ": "ДНІПРОПЕТРОВСЬК",
        "ЛЕНІНСЬКИЙ": "ДНІПРОПЕТРОВСЬК",
        "МЕТАЛУРГІЙНИЙ": "КРИВИЙ РІГ",
        "НОВОКОДАЦЬКИЙ": "ДНІПРО",
        "ПОКРОВСЬКИЙ": "КРИВИЙ РІГ",
        "ПІВДЕННИЙ": "КАМ’ЯНСЬКЕ",
        "САКСАГАНСЬКИЙ": "КРИВИЙ РІГ",
        "САМАРСЬКИЙ": "ДНІПРО",
        "СОБОРНИЙ": "ДНІПРО",
        "ТЕРНІВСЬКИЙ": "КРИВИЙ РІГ",
        "ЦЕНТРАЛЬНИЙ": "ДНІПРО",
        "ЦЕНТРАЛЬНО-МІСЬКИЙ": "КРИВИЙ РІГ",
        "ЧЕЧЕЛІВСЬКИЙ": "ДНІПРО",
        "ШЕВЧЕНКІВСЬКИЙ": "ДНІПРО",
        "ІНГУЛЕЦЬКИЙ": "КРИВИЙ РІГ",
        "ІНДУСТРІАЛЬНИЙ": "ДНІПРО"
    },
    "ЖИТОМИРСЬКА": {
        "БОГУНСЬКИЙ": "ЖИТОМИР",
        "КОРОЛЬОВСЬКИЙ": "ЖИТОМИР"
    },
    "ЗАПОРІЗЬКА": {
        "ВОЗНЕСЕНІВСЬКИЙ": "ЗАПОРІЖЖЯ",
        "ДНІПРОВСЬКИЙ": "ЗАПОРІЖЖЯ",
        "ЖОВТНЕВИЙ": "ЗАПОРІЖЖЯ",
        "ЗАВОДСЬКИЙ": "ЗАПОРІЖЖЯ",
        "КОМУНАРСЬКИЙ": "ЗАПОРІЖЖЯ",
        "ЛЕНІНСЬКИЙ": "ЗАПОРІЖЖЯ",
        "ОЛЕКСАНДРІВСЬКИЙ": "ЗАПОРІЖЖЯ",
        "ОРДЖОНІКІДЗЕВСЬКИЙ": "ЗАПОРІЖЖЯ",
        "ХОРТИЦЬКИЙ": "ЗАПОРІЖЖЯ",
        "ШЕВЧЕНКІВСЬКИЙ": "ЗАПОРІЖЖЯ"
    },
    "КІРОВОГРАДСЬКА": {
        "КІРОВСЬКИЙ": "КІРОВОГРАД",
        "ЛЕНІНСЬКИЙ": "КІРОВОГРАД",
        "ПОДІЛЬСЬКИЙ": "КРОПИВНИЦЬКИЙ",
        "ФОРТЕЧНИЙ": "КРОПИВНИЦЬКИЙ"
    },
    "ЛУГАНСЬКА": {
        "АРТЕМІВСЬКИЙ": "ЛУГАНСЬК",
        "ЖОВТНЕВИЙ": "ЛУГАНСЬК",
        "КАМ’ЯНОБРІДСЬКИЙ": "ЛУГАНСЬК",
        "ЛЕНІНСЬКИЙ": "ЛУГАНСЬК"
    },
    "ЛЬВІВСЬКА": {
        "ГАЛИЦЬКИЙ": "ЛЬВІВ",
        "ЗАЛІЗНИЧНИЙ": "ЛЬВІВ",
        "ЛИЧАКІВСЬКИЙ": "ЛЬВІВ",
        "СИХІВСЬКИЙ": "ЛЬВІВ",
        "ФРАНКІВСЬКИЙ": "ЛЬВІВ",
        "ШЕВЧЕНКІВСЬКИЙ": "ЛЬВІВ"
    },
    "МИКОЛАЇВСЬКА": {
        "ЗАВОДСЬКИЙ": "МИКОЛАЇВ",
        "ІНГУЛЬСЬКИЙ": "МИКОЛАЇВ",
        "КОРАБЕЛЬНИЙ": "МИКОЛАЇВ",
        "ЛЕНІНСЬКИЙ": "МИКОЛАЇВ",
        "ЦЕНТРАЛЬНИЙ": "МИКОЛАЇВ"
    },
    "ОДЕСЬКА": {
        "КИЇВСЬКИЙ": "ОДЕСА",
        "МАЛИНОВСЬКИЙ": "ОДЕСА",
        "ПРИМОРСЬКИЙ": "ОДЕСА",
        "СУВОРОВСЬКИЙ": "ОДЕСА",
        "СОНЯЧНИЙ КУРОРТНИЙ": "БІЛГОРОД-ДНІСТРОВСЬКИЙ",
    },
    "ПОЛТАВСЬКА": {
        "КИЇВСЬКИЙ": "ПОЛТАВА",
        "ЛЕНІНСЬКИЙ": "ПОЛТАВА",
        "ОКТЯБРСЬКИЙ": "ПОЛТАВА",
        "ПОДІЛЬСЬКИЙ": "ПОЛТАВА",
        "ШЕВЧЕНКІВСЬКИЙ": "ПОЛТАВА",
        "АВТОЗАВОДСЬКИЙ": "КРЕМЕНЧУК",
        "КРЮКІВСЬКИЙ": "КРЕМЕНЧУК"
    },
    "АВТОНОМНА РЕСПУБЛІКА КРИМ": {
        "ЗАЛІЗНИЧНИЙ": "СІМФЕРОПОЛЬ",
        "КИЇВСЬКИЙ": "СІМФЕРОПОЛЬ",
        "ЦЕНТРАЛЬНИЙ": "СІМФЕРОПОЛЬ",
        "СЕВЕРО-ВОСТОЧНИЙ": "САКИ",
    },
    "СУМСЬКА": {
        "ЗАРІЧНИЙ": "СУМИ",
        "КОВПАКІВСЬКИЙ": "СУМИ"
    },
    "ХАРКІВСЬКА": {
        "ДЗЕРЖИНСЬКИЙ": "ХАРКІВ",
        "ЖОВТНЕВИЙ": "ХАРКІВ",
        "КОМІНТЕРНІВСЬКИЙ": "ХАРКІВ",
        "ЛЕНІНСЬКИЙ": "ХАРКІВ",
        "ОРДЖОНІКІДЗЕВСЬКИЙ": "ХАРКІВ",
        "ФРУНЗЕНСЬКИЙ": "ХАРКІВ",
        "ЧЕРВОНОЗАВОДСЬКИЙ": "ХАРКІВ",
        "ІНДУСТРІАЛЬНИЙ": "ХАРКІВ",
        "КИЇВСЬКИЙ": "ХАРКІВ",
        "МОСКОВСЬКИЙ": "ХАРКІВ",
        "НЕМИШЛЯНСЬКИЙ": "ХАРКІВ",
        "НОВОБАВАРСЬКИЙ": "ХАРКІВ",
        "ОСНОВ’ЯНСЬКИЙ": "ХАРКІВ",
        "СЛОБІДСЬКИЙ": "ХАРКІВ",
        "ХОЛОДНОГІРСЬКИЙ": "ХАРКІВ",
        "ШЕВЧЕНКІВСЬКИЙ": "ХАРКІВ"
    },
    "ХЕРСОНСЬКА": {
        "КОМСОМОЛЬСЬКИЙ": "ХЕРСОН",
        "ДНІПРОВСЬКИЙ": "ХЕРСОН",
        "КОРАБЕЛЬНИЙ": "ХЕРСОН",
        "СУВОРОВСЬКИЙ": "ХЕРСОН"
    },
    "ЧЕРКАСЬКА": {
        "ПРИДНІПРОВСЬКИЙ": "ЧЕРКАСИ",
        "СОСНІВСЬКИЙ": "ЧЕРКАСИ"
    },
    "ЧЕРНІВЕЦЬКА": {
        "ПЕРШОТРАВНЕВИЙ": "ЧЕРНІВЦІ",
        "САДГІРСЬКИЙ": "ЧЕРНІВЦІ",
        "ШЕВЧЕНКІВСЬКИЙ": "ЧЕРНІВЦІ"
    },
    "ЧЕРНІГІВСЬКА": {
        "ДЕСНЯНСЬКИЙ": "ЧЕРНІГІВ",
        "НОВОЗАВОДСЬКИЙ": "ЧЕРНІГІВ"
    },
}

city_rajons2 = {
    "ЗАМОСТЯНСЬКИЙ": [
        "ВІННИЦЯ"
    ],
    "ЛЕНІНСЬКИЙ": [
        "ВІННИЦЯ",
        "ДНІПРОПЕТРОВСЬК",
        "ДОНЕЦЬК",
        "ЗАПОРІЖЖЯ",
        "КІРОВОГРАД",
        "ЛУГАНСЬК",
        "МИКОЛАЇВ",
        "ПОЛТАВА",
        "СЕВАСТОПОЛЬ",
        "ХАРКІВ"
    ],
    "СТАРОМІСЬКИЙ": [
        "ВІННИЦЯ"
    ],
    "КАЛІНІНСЬКИЙ": [
        "ГОРЛІВКА",
        "ДОНЕЦЬК"
    ],
    "МИКИТІВСЬКИЙ": [
        "ГОРЛІВКА"
    ],
    "ЦЕНТРАЛЬНО-МІСЬКИЙ": [
        "ГОРЛІВКА",
        "КРИВИЙ РІГ"
    ],
    "АМУР-НИЖНЬОДНІПРОВСЬКИЙ": [
        "ДНІПРО", "ДНІПРОПЕТРОВСЬК"
    ],
    "НОВОКОДАЦЬКИЙ": [
        "ДНІПРО"
    ],
    "САМАРСЬКИЙ": [
        "ДНІПРО"
    ],
    "СОБОРНИЙ": [
        "ДНІПРО"
    ],
    "ЦЕНТРАЛЬНИЙ": [
        "ДНІПРО",
        "МАРІУПОЛЬ",
        "МИКОЛАЇВ",
        "СІМФЕРОПОЛЬ"
    ],
    "ЧЕЧЕЛІВСЬКИЙ": [
        "ДНІПРО"
    ],
    "ШЕВЧЕНКІВСЬКИЙ": [
        "ДНІПРО",
        "ЗАПОРІЖЖЯ",
        "ЛЬВІВ",
        "ПОЛТАВА",
        "ХАРКІВ",
        "ЧЕРНІВЦІ"
    ],
    "ІНДУСТРІАЛЬНИЙ": [
        "ДНІПРО",
        "ХАРКІВ"
    ],
    "БАГЛІЙСЬКИЙ": [
        "ДНІПРОДЗЕРЖИНСЬК"
    ],
    "БАБУШКІНСЬКИЙ": [
        "ДНІПРОПЕТРОВСЬК"
    ],
    "ЖОВТНЕВИЙ": [
        "ДНІПРОПЕТРОВСЬК",
        "ЗАПОРІЖЖЯ",
        "КРИВИЙ РІГ",
        "ЛУГАНСЬК",
        "МАРІУПОЛЬ",
        "ХАРКІВ"
    ],
    "КРАСНОГВАРДІЙСЬКИЙ": [
        "ДНІПРОПЕТРОВСЬК"
    ],
    "КІРОВСЬКИЙ": [
        "ДНІПРОПЕТРОВСЬК",
        "ДОНЕЦЬК",
        "КІРОВОГРАД",
        "МАКІЇВКА"
    ],
    "БУДЬОННІВСЬКИЙ": [
        "ДОНЕЦЬК"
    ],
    "ВОРОШИЛОВСЬКИЙ": [
        "ДОНЕЦЬК"
    ],
    "КИЇВСЬКИЙ": [
        "ДОНЕЦЬК",
        "ОДЕСА",
        "ПОЛТАВА",
        "СІМФЕРОПОЛЬ",
        "ХАРКІВ"
    ],
    "КУЙБИШЕВСЬКИЙ": [
        "ДОНЕЦЬК"
    ],
    "ПЕТРОВСЬКИЙ": [
        "ДОНЕЦЬК"
    ],
    "ПРОЛЕТАРСЬКИЙ": [
        "ДОНЕЦЬК"
    ],
    "БОГУНСЬКИЙ": [
        "ЖИТОМИР"
    ],
    "КОРОЛЬОВСЬКИЙ": [
        "ЖИТОМИР"
    ],
    "ВОЗНЕСЕНІВСЬКИЙ": [
        "ЗАПОРІЖЖЯ"
    ],
    "ДНІПРОВСЬКИЙ": [
        "ЗАПОРІЖЖЯ",
        "КАМ’ЯНСЬКЕ",
        "ХЕРСОН"
    ],
    "ЗАВОДСЬКИЙ": [
        "ЗАПОРІЖЖЯ",
        "КАМ’ЯНСЬКЕ",
        "МИКОЛАЇВ"
    ],
    "КОМУНАРСЬКИЙ": [
        "ЗАПОРІЖЖЯ"
    ],
    "ОЛЕКСАНДРІВСЬКИЙ": [
        "ЗАПОРІЖЖЯ"
    ],
    "ОРДЖОНІКІДЗЕВСЬКИЙ": [
        "ЗАПОРІЖЖЯ",
        "МАРІУПОЛЬ",
        "ХАРКІВ"
    ],
    "ХОРТИЦЬКИЙ": [
        "ЗАПОРІЖЖЯ"
    ],
    "ПІВДЕННИЙ": [
        "КАМ’ЯНСЬКЕ"
    ],
    "АВТОЗАВОДСЬКИЙ": [
        "КРЕМЕНЧУК"
    ],
    "КРЮКІВСЬКИЙ": [
        "КРЕМЕНЧУК"
    ],
    "ДЗЕРЖИНСЬКИЙ": [
        "КРИВИЙ РІГ",
        "ХАРКІВ"
    ],
    "ДОВГИНЦІВСЬКИЙ": [
        "КРИВИЙ РІГ"
    ],
    "МЕТАЛУРГІЙНИЙ": [
        "КРИВИЙ РІГ"
    ],
    "ПОКРОВСЬКИЙ": [
        "КРИВИЙ РІГ"
    ],
    "САКСАГАНСЬКИЙ": [
        "КРИВИЙ РІГ"
    ],
    "ТЕРНІВСЬКИЙ": [
        "КРИВИЙ РІГ"
    ],
    "ІНГУЛЕЦЬКИЙ": [
        "КРИВИЙ РІГ"
    ],
    "ПОДІЛЬСЬКИЙ": [
        "КРОПИВНИЦЬКИЙ",
        "ПОЛТАВА"
    ],
    "ФОРТЕЧНИЙ": [
        "КРОПИВНИЦЬКИЙ"
    ],
    "АРТЕМІВСЬКИЙ": [
        "ЛУГАНСЬК"
    ],
    "КАМ’ЯНОБРІДСЬКИЙ": [
        "ЛУГАНСЬК"
    ],
    "ГАЛИЦЬКИЙ": [
        "ЛЬВІВ"
    ],
    "ЗАЛІЗНИЧНИЙ": [
        "ЛЬВІВ",
        "СІМФЕРОПОЛЬ"
    ],
    "ЛИЧАКІВСЬКИЙ": [
        "ЛЬВІВ"
    ],
    "СИХІВСЬКИЙ": [
        "ЛЬВІВ"
    ],
    "ФРАНКІВСЬКИЙ": [
        "ЛЬВІВ"
    ],
    "ГІРНИЦЬКИЙ": [
        "МАКІЇВКА"
    ],
    "СОВЄТСЬКИЙ": [
        "МАКІЇВКА",
        "МАКІЇВКА"
    ],
    "ЧЕРВОНОГВАРДІЙСЬКИЙ": [
        "МАКІЇВКА",
        "МАКІЇВКА"
    ],
    "КАЛЬМІУСЬКИЙ": [
        "МАРІУПОЛЬ"
    ],
    "ЛІВОБЕРЕЖНИЙ": [
        "МАРІУПОЛЬ"
    ],
    "ПРИМОРСЬКИЙ": [
        "МАРІУПОЛЬ",
        "ОДЕСА"
    ],
    "ІЛЛІЧІВСЬКИЙ": [
        "МАРІУПОЛЬ"
    ],
    "КОРАБЕЛЬНИЙ": [
        "МИКОЛАЇВ",
        "ХЕРСОН"
    ],
    "ІНГУЛЬСЬКИЙ": [
        "МИКОЛАЇВ"
    ],
    "МАЛИНОВСЬКИЙ": [
        "ОДЕСА"
    ],
    "СУВОРОВСЬКИЙ": [
        "ОДЕСА",
        "ХЕРСОН"
    ],
    "ОКТЯБРСЬКИЙ": [
        "ПОЛТАВА"
    ],
    "ЗАРІЧНИЙ": [
        "СУМИ"
    ],
    "КОВПАКІВСЬКИЙ": [
        "СУМИ"
    ],
    "КОМІНТЕРНІВСЬКИЙ": [
        "ХАРКІВ"
    ],
    "МОСКОВСЬКИЙ": [
        "ХАРКІВ"
    ],
    "НЕМИШЛЯНСЬКИЙ": [
        "ХАРКІВ"
    ],
    "НОВОБАВАРСЬКИЙ": [
        "ХАРКІВ"
    ],
    "ОСНОВ’ЯНСЬКИЙ": [
        "ХАРКІВ"
    ],
    "СЛОБІДСЬКИЙ": [
        "ХАРКІВ"
    ],
    "ФРУНЗЕНСЬКИЙ": [
        "ХАРКІВ"
    ],
    "ХОЛОДНОГІРСЬКИЙ": [
        "ХАРКІВ"
    ],
    "ЧЕРВОНОЗАВОДСЬКИЙ": [
        "ХАРКІВ"
    ],
    "КОМСОМОЛЬСЬКИЙ": [
        "ХЕРСОН"
    ],
    "ПРИДНІПРОВСЬКИЙ": [
        "ЧЕРКАСИ"
    ],
    "СОСНІВСЬКИЙ": [
        "ЧЕРКАСИ"
    ],
    "ПЕРШОТРАВНЕВИЙ": [
        "ЧЕРНІВЦІ"
    ],
    "САДГІРСЬКИЙ": [
        "ЧЕРНІВЦІ"
    ],
    "ДЕСНЯНСЬКИЙ": [
        "ЧЕРНІГІВ"
    ],
    "НОВОЗАВОДСЬКИЙ": [
        "ЧЕРНІГІВ"
    ]
}

raj_etalon = {
  "Є": [
    "ЄЛАНЕЦЬКИЙ",
    "ЄМІЛЬЧИНСЬКИЙ"
  ],
  "І": [
    "ІРПІНСЬКИЙ",
    "ІВАНИЧІВСЬКИЙ",
    "ІВАНКІВСЬКИЙ",
    "ІВАНІВСЬКИЙ",
    "ІЗМАЇЛЬСЬКИЙ",
    "ІЗЮМСЬКИЙ",
    "ІЗЯСЛАВСЬКИЙ",
    "ІЛЛІНЕЦЬКИЙ",
    "ІЛЛІЧІВСЬКИЙ",
    "ІНГУЛЕЦЬКИЙ",
    "ІНГУЛЬСЬКИЙ",
    "ІНДУСТРІАЛЬНИЙ",
    "ІРШАВСЬКИЙ",
    "ІЧНЯНСЬКИЙ"
  ],
  "А": [
    "АВТОЗАВОДСЬКИЙ",
    "АКАДЕМІЧНИЙ",
    "АМВРОСІЇВСЬКИЙ",
    "АМУР-НИЖНЬОДНІПРОВСЬКИЙ",
    "АНАНЬЇВСЬКИЙ",
    "АНДРУШІВСЬКИЙ",
    "АНТРАЦИТІВСЬКИЙ",
    "АПОСТОЛІВСЬКИЙ",
    "АРБУЗИНСЬКИЙ",
    "АРТЕМІВСЬКИЙ",
    "АРЦИЗЬКИЙ"
  ],
  "Б": [
    "БАБУШКІНСЬКИЙ",
    "БАГЛІЙСЬКИЙ",
    "БАЛАКЛАВСЬКИЙ",
    "БАЛАКЛІЙСЬКИЙ",
    "БАЛТСЬКИЙ",
    "БАРАНІВСЬКИЙ",
    "БАРВІНКІВСЬКИЙ",
    "БАРИШІВСЬКИЙ",
    "БАРСЬКИЙ",
    "БАХМАЦЬКИЙ",
    "БАХМУТСЬКИЙ",
    "БАХЧИСАРАЙСЬКИЙ",
    "БАШТАНСЬКИЙ",
    "БЕРДИЧІВСЬКИЙ",
    "БЕРДЯНСЬКИЙ",
    "БЕРЕГІВСЬКИЙ",
    "БЕРЕЖАНСЬКИЙ",
    "БЕРЕЗАНСЬКИЙ",
    "БЕРЕЗНЕГУВАТСЬКИЙ",
    "БЕРЕЗНІВСЬКИЙ",
    "БЕРЕЗІВСЬКИЙ",
    "БЕРИСЛАВСЬКИЙ",
    "БЕРШАДСЬКИЙ",
    "БЛАГОВІЩЕНСЬКИЙ",
    "БЛИЗНЮКІВСЬКИЙ",
    "БОБРИНЕЦЬКИЙ",
    "БОБРОВИЦЬКИЙ",
    "БОГОДУХІВСЬКИЙ",
    "БОГОРОДЧАНСЬКИЙ",
    "БОГУНСЬКИЙ",
    "БОГУСЛАВСЬКИЙ",
    "БОЙКІВСЬКИЙ",
    "БОЛГРАДСЬКИЙ",
    "БОРЗНЯНСЬКИЙ",
    "БОРИСПІЛЬСЬКИЙ",
    "БОРОДЯНСЬКИЙ",
    "БОРЩІВСЬКИЙ",
    "БОРІВСЬКИЙ",
    "БРАТСЬКИЙ",
    "БРОВАРСЬКИЙ",
    "БРОДІВСЬКИЙ",
    "БРУСИЛІВСЬКИЙ",
    "БУДЬОННІВСЬКИЙ",
    "БУРИНСЬКИЙ",
    "БУСЬКИЙ",
    "БУЧАЦЬКИЙ",
    "БІЛГОРОД-ДНІСТРОВСЬКИЙ",
    "БІЛОВОДСЬКИЙ",
    "БІЛОГІРСЬКИЙ",
    "БІЛОЗЕРСЬКИЙ",
    "БІЛОКУРАКИНСЬКИЙ",
    "БІЛОПІЛЬСЬКИЙ",
    "БІЛОЦЕРКІВСЬКИЙ",
    "БІЛЬМАЦЬКИЙ",
    "БІЛЯЇВСЬКИЙ"
  ],
  "В": [
    "ВАЛКІВСЬКИЙ",
    "ВАРВИНСЬКИЙ",
    "ВАСИЛЬКІВСЬКИЙ",
    "ВАСИЛІВСЬКИЙ",
    "ВАТУТІНСЬКИЙ",
    "ВЕЛИКОБАГАЧАНСЬКИЙ",
    "ВЕЛИКОБЕРЕЗНЯНСЬКИЙ",
    "ВЕЛИКОБУРЛУЦЬКИЙ",
    "ВЕЛИКОБІЛОЗЕРСЬКИЙ",
    "ВЕЛИКОЛЕПЕТИСЬКИЙ",
    "ВЕЛИКОМИХАЙЛІВСЬКИЙ",
    "ВЕЛИКОНОВОСІЛКІВСЬКИЙ",
    "ВЕЛИКООЛЕКСАНДРІВСЬКИЙ",
    "ВЕЛИКОПИСАРІВСЬКИЙ",
    "ВЕРХНЬОДНІПРОВСЬКИЙ",
    "ВЕРХНЬОРОГАЧИЦЬКИЙ",
    "ВЕРХОВИНСЬКИЙ",
    "ВЕСЕЛИНІВСЬКИЙ",
    "ВЕСЕЛІВСЬКИЙ",
    "ВИЖНИЦЬКИЙ",
    "ВИНОГРАДІВСЬКИЙ",
    "ВИСОКОПІЛЬСЬКИЙ",
    "ВИШГОРОДСЬКИЙ",
    "ВОВЧАНСЬКИЙ",
    "ВОЗНЕСЕНСЬКИЙ",
    "ВОЗНЕСЕНІВСЬКИЙ",
    "ВОЛНОВАСЬКИЙ",
    "ВОЛОВЕЦЬКИЙ",
    "ВОЛОДАРСЬКИЙ",
    "ВОЛОДАРСЬКО-ВОЛИНСЬКИЙ",
    "ВОЛОДИМИР-ВОЛИНСЬКИЙ",
    "ВОЛОДИМИРЕЦЬКИЙ",
    "ВОЛОЧИСЬКИЙ",
    "ВОРОШИЛОВСЬКИЙ",
    "ВРАДІЇВСЬКИЙ",
    "ВІЛЬНЯНСЬКИЙ",
    "ВІЛЬШАНСЬКИЙ",
    "ВІННИЦЬКИЙ",
    "ВІНЬКОВЕЦЬКИЙ",
    "ВІТОВСЬКИЙ"
  ],
  "Г": [
    "ГАГАРІНСЬКИЙ",
    "ГАДЯЦЬКИЙ",
    "ГАЙВОРОНСЬКИЙ",
    "ГАЙСИНСЬКИЙ",
    "ГАЛИЦЬКИЙ",
    "ГЕНІЧЕСЬКИЙ",
    "ГЕРЦАЇВСЬКИЙ",
    "ГЛИБОЦЬКИЙ",
    "ГЛОБИНСЬКИЙ",
    "ГЛУХІВСЬКИЙ",
    "ГОЛОВАНІВСЬКИЙ",
    "ГОЛОПРИСТАНСЬКИЙ",
    "ГОЛОСІЇВСЬКИЙ",
    "ГОРНОСТАЇВСЬКИЙ",
    "ГОРОДЕНКІВСЬКИЙ",
    "ГОРОДИЩЕНСЬКИЙ",
    "ГОРОДНЯНСЬКИЙ",
    "ГОРОДОЦЬКИЙ",
    "ГОРОХІВСЬКИЙ",
    "ГОЩАНСЬКИЙ",
    "ГРЕБІНКІВСЬКИЙ",
    "ГУЛЯЙПІЛЬСЬКИЙ",
    "ГУСЯТИНСЬКИЙ",
    "ГІРНИЦЬКИЙ"
  ],
  "Д": [
    "ДЖАНКОЙСЬКИЙ",
    "ДАРНИЦЬКИЙ",
    "ДВОРІЧАНСЬКИЙ",
    "ДЕМИДІВСЬКИЙ",
    "ДЕРАЖНЯНСЬКИЙ",
    "ДЕРГАЧІВСЬКИЙ",
    "ДЕСНЯНСЬКИЙ",
    "ДЗЕРЖИНСЬКИЙ",
    "ДИКАНСЬКИЙ",
    "ДНІПРОВСЬКИЙ",
    "ДНІПРОПЕТРОВСЬКИЙ",
    "ДОБРОВЕЛИЧКІВСЬКИЙ",
    "ДОБРОПІЛЬСЬКИЙ",
    "ДОВГИНЦІВСЬКИЙ",
    "ДОВЖАНСЬКИЙ",
    "ДОЛИНСЬКИЙ",
    "ДОМАНІВСЬКИЙ",
    "ДРАБІВСЬКИЙ",
    "ДРОГОБИЦЬКИЙ",
    "ДУБЕНСЬКИЙ",
    "ДУБРОВИЦЬКИЙ",
    "ДУНАЄВЕЦЬКИЙ"
  ],
  "Ж": [
    "ЖАШКІВСЬКИЙ",
    "ЖЕЛЄЗНОДОРОЖНИЙ",
    "ЖИДАЧІВСЬКИЙ",
    "ЖИТОМИРСЬКИЙ",
    "ЖМЕРИНСЬКИЙ",
    "ЖОВКІВСЬКИЙ",
    "ЖОВТНЕВИЙ"
  ],
  "З": [
    "ЗАВОДСЬКИЙ",
    "ЗАЛІЗНИЧНИЙ",
    "ЗАЛІЩИЦЬКИЙ",
    "ЗАМОСТЯНСЬКИЙ",
    "ЗАПОРІЗЬКИЙ",
    "ЗАРІЧНЕНСЬКИЙ",
    "ЗАРІЧНИЙ",
    "ЗАСТАВНІВСЬКИЙ",
    "ЗАХАРІВСЬКИЙ",
    "ЗАЧЕПИЛІВСЬКИЙ",
    "ЗБАРАЗЬКИЙ",
    "ЗБОРІВСЬКИЙ",
    "ЗВЕНИГОРОДСЬКИЙ",
    "ЗГУРІВСЬКИЙ",
    "ЗДОЛБУНІВСЬКИЙ",
    "ЗМІЇВСЬКИЙ",
    "ЗНАМ’ЯНСЬКИЙ",
    "ЗОЛОТОНІСЬКИЙ",
    "ЗОЛОЧІВСЬКИЙ",
    "ЗІНЬКІВСЬКИЙ"
  ],
  "К": [
    "КАГАРЛИЦЬКИЙ",
    "КАЗАНКІВСЬКИЙ",
    "КАЛАНЧАЦЬКИЙ",
    "КАЛИНІВСЬКИЙ",
    "КАЛУСЬКИЙ",
    "КАЛЬМІУСЬКИЙ",
    "КАЛІНІНСЬКИЙ",
    "КАМІНЬ-КАШИРСЬКИЙ",
    "КАМ’ЯНЕЦЬ-ПОДІЛЬСЬКИЙ",
    "КАМ’ЯНКА-БУЗЬКИЙ",
    "КАМ’ЯНОБРІДСЬКИЙ",
    "КАМ’ЯНСЬКИЙ",
    "КАМ’ЯНСЬКО-ДНІПРОВСЬКИЙ",
    "КАНІВСЬКИЙ",
    "КАРЛІВСЬКИЙ",
    "КАТЕРИНОПІЛЬСЬКИЙ",
    "КАХОВСЬКИЙ",
    "КЕГИЧІВСЬКИЙ",
    "КЕЛЬМЕНЕЦЬКИЙ",
    "КИЄВО-СВЯТОШИНСЬКИЙ",
    "КИЇВСЬКИЙ",
    "КОБЕЛЯЦЬКИЙ",
    "КОВЕЛЬСЬКИЙ",
    "КОВПАКІВСЬКИЙ",
    "КОДИМСЬКИЙ",
    "КОЗЕЛЕЦЬКИЙ",
    "КОЗЕЛЬЩИНСЬКИЙ",
    "КОЗЯТИНСЬКИЙ",
    "КОЗІВСЬКИЙ",
    "КОЛОМАЦЬКИЙ",
    "КОЛОМИЙСЬКИЙ",
    "КОМПАНІЇВСЬКИЙ",
    "КОМСОМОЛЬСЬКИЙ",
    "КОМУНАРСЬКИЙ",
    "КОМІНТЕРНІВСЬКИЙ",
    "КОНОТОПСЬКИЙ",
    "КОРАБЕЛЬНИЙ",
    "КОРЕЦЬКИЙ",
    "КОРОЛЬОВСЬКИЙ",
    "КОРОПСЬКИЙ",
    "КОРОСТЕНСЬКИЙ",
    "КОРОСТИШІВСЬКИЙ",
    "КОРСУНЬ-ШЕВЧЕНКІВСЬКИЙ",
    "КОРЮКІВСЬКИЙ",
    "КОСТОПІЛЬСЬКИЙ",
    "КОСТЯНТИНІВСЬКИЙ",
    "КОСІВСЬКИЙ",
    "КОТЕЛЕВСЬКИЙ",
    "КОТОВСЬКИЙ",
    "КРАСИЛІВСЬКИЙ",
    "КРАСНОАРМІЙСЬКИЙ",
    "КРАСНОГВАРДІЙСЬКИЙ",
    "КРАСНОГРАДСЬКИЙ",
    "КРАСНОДОНСЬКИЙ",
    "КРАСНОКУТСЬКИЙ",
    "КРАСНОЛИМАНСЬКИЙ",
    "КРАСНООКНЯНСЬКИЙ",
    "КРАСНОПЕРЕКОПСЬКИЙ",
    "КРАСНОПІЛЬСЬКИЙ",
    "КРЕМЕНЕЦЬКИЙ",
    "КРЕМЕНЧУЦЬКИЙ",
    "КРЕМІНСЬКИЙ",
    "КРИВООЗЕРСЬКИЙ",
    "КРИВОРІЗЬКИЙ",
    "КРИЖОПІЛЬСЬКИЙ",
    "КРИНИЧАНСЬКИЙ",
    "КРОЛЕВЕЦЬКИЙ",
    "КРОПИВНИЦЬКИЙ",
    "КРЮКІВСЬКИЙ",
    "КУЙБИШЕВСЬКИЙ",
    "КУЛИКІВСЬКИЙ",
    "КУП’ЯНСЬКИЙ",
    "КІВЕРЦІВСЬКИЙ",
    "КІЛІЙСЬКИЙ",
    "КІРОВОГРАДСЬКИЙ",
    "КІРОВСЬКИЙ",
    "КІЦМАНСЬКИЙ"
  ],
  "Л": [
    "ЛАНОВЕЦЬКИЙ",
    "ЛЕБЕДИНСЬКИЙ",
    "ЛЕНІНГРАДСЬКИЙ",
    "ЛЕНІНСЬКИЙ",
    "ЛЕТИЧІВСЬКИЙ",
    "ЛИМАНСЬКИЙ",
    "ЛИПОВЕЦЬКИЙ",
    "ЛИПОВОДОЛИНСЬКИЙ",
    "ЛИСЯНСЬКИЙ",
    "ЛИЧАКІВСЬКИЙ",
    "ЛОЗІВСЬКИЙ",
    "ЛОКАЧИНСЬКИЙ",
    "ЛОХВИЦЬКИЙ",
    "ЛУБЕНСЬКИЙ",
    "ЛУГИНСЬКИЙ",
    "ЛУТУГИНСЬКИЙ",
    "ЛУЦЬКИЙ",
    "ЛЮБАРСЬКИЙ",
    "ЛЮБАШІВСЬКИЙ",
    "ЛЮБЕШІВСЬКИЙ",
    "ЛЮБОМЛЬСЬКИЙ",
    "ЛІВОБЕРЕЖНИЙ",
    "ЛІТИНСЬКИЙ"
  ],
  "М": [
    "МАГДАЛИНІВСЬКИЙ",
    "МАКАРІВСЬКИЙ",
    "МАЛИНОВСЬКИЙ",
    "МАЛИНСЬКИЙ",
    "МАЛОВИСКІВСЬКИЙ",
    "МАНГУШСЬКИЙ",
    "МАНЕВИЦЬКИЙ",
    "МАНЬКІВСЬКИЙ",
    "МАРКІВСЬКИЙ",
    "МАР’ЇНСЬКИЙ",
    "МАШІВСЬКИЙ",
    "МЕЖІВСЬКИЙ",
    "МЕЛІТОПОЛЬСЬКИЙ",
    "МЕНСЬКИЙ",
    "МЕТАЛУРГІЙНИЙ",
    "МИКИТІВСЬКИЙ",
    "МИКОЛАЇВСЬКИЙ",
    "МИРГОРОДСЬКИЙ",
    "МИРОНІВСЬКИЙ",
    "МИХАЙЛІВСЬКИЙ",
    "МЛИНІВСЬКИЙ",
    "МОГИЛІВ-ПОДІЛЬСЬКИЙ",
    "МОНАСТИРИСЬКИЙ",
    "МОНАСТИРИЩЕНСЬКИЙ",
    "МОСКОВСЬКИЙ",
    "МОСТИСЬКИЙ",
    "МУКАЧІВСЬКИЙ",
    "МУРОВАНОКУРИЛОВЕЦЬКИЙ",
    "МІЖГІРСЬКИЙ",
    "МІЛОВСЬКИЙ",
    "МІНСЬКИЙ"
  ],
  "Н": [
    "НАДВІРНЯНСЬКИЙ",
    "НАРОДИЦЬКИЙ",
    "НАХІМОВСЬКИЙ",
    "НЕДРИГАЙЛІВСЬКИЙ",
    "НЕМИРІВСЬКИЙ",
    "НЕМИШЛЯНСЬКИЙ",
    "НИЖНЬОГІРСЬКИЙ",
    "НИЖНЬОСІРОГОЗЬКИЙ",
    "НОВГОРОД-СІВЕРСЬКИЙ",
    "НОВГОРОДКІВСЬКИЙ",
    "НОВОАЗОВСЬКИЙ",
    "НОВОАЙДАРСЬКИЙ",
    "НОВОАРХАНГЕЛЬСЬКИЙ",
    "НОВОБАВАРСЬКИЙ",
    "НОВОБУЗЬКИЙ",
    "НОВОВОДОЛАЗЬКИЙ",
    "НОВОВОРОНЦОВСЬКИЙ",
    "НОВОГРАД-ВОЛИНСЬКИЙ",
    "НОВОЗАВОДСЬКИЙ",
    "НОВОКОДАЦЬКИЙ",
    "НОВОМИКОЛАЇВСЬКИЙ",
    "НОВОМИРГОРОДСЬКИЙ",
    "НОВОМОСКОВСЬКИЙ",
    "НОВООДЕСЬКИЙ",
    "НОВОПСКОВСЬКИЙ",
    "НОВОСАНЖАРСЬКИЙ",
    "НОВОСЕЛИЦЬКИЙ",
    "НОВОТРОЇЦЬКИЙ",
    "НОВОУКРАЇНСЬКИЙ",
    "НОВОУШИЦЬКИЙ",
    "НОСІВСЬКИЙ",
    "НІЖИНСЬКИЙ",
    "НІКОЛЬСЬКИЙ",
    "НІКОПОЛЬСЬКИЙ"
  ],
  "О": [
    "ОБОЛОНСЬКИЙ",
    "ОБУХІВСЬКИЙ",
    "ОВРУЦЬКИЙ",
    "ОВІДІОПОЛЬСЬКИЙ",
    "ОКНЯНСЬКИЙ",
    "ОКТЯБРСЬКИЙ",
    "ОЛЕВСЬКИЙ",
    "ОЛЕКСАНДРІВСЬКИЙ",
    "ОЛЕКСАНДРІЙСЬКИЙ",
    "ОЛЕШКІВСЬКИЙ",
    "ОНУФРІЇВСЬКИЙ",
    "ОРАТІВСЬКИЙ",
    "ОРДЖОНІКІДЗЕВСЬКИЙ",
    "ОРЖИЦЬКИЙ",
    "ОРІХІВСЬКИЙ",
    "ОСНОВ’ЯНСЬКИЙ",
    "ОСТРОЗЬКИЙ",
    "ОХТИРСЬКИЙ",
    "ОЧАКІВСЬКИЙ"
  ],
  "П": [
    "ПАВЛОГРАДСЬКИЙ",
    "ПЕРВОМАЙСЬКИЙ",
    "ПЕРЕВАЛЬСЬКИЙ",
    "ПЕРЕМИШЛЯНСЬКИЙ",
    "ПЕРЕЧИНСЬКИЙ",
    "ПЕРЕЯСЛАВ-ХМЕЛЬНИЦЬКИЙ",
    "ПЕРШОТРАВНЕВИЙ",
    "ПЕТРИКІВСЬКИЙ",
    "ПЕТРОВСЬКИЙ",
    "ПЕТРОПАВЛІВСЬКИЙ",
    "ПЕТРІВСЬКИЙ",
    "ПЕЧЕНІЗЬКИЙ",
    "ПЕЧЕРСЬКИЙ",
    "ПИРЯТИНСЬКИЙ",
    "ПОГРЕБИЩЕНСЬКИЙ",
    "ПОДІЛЬСЬКИЙ",
    "ПОКРОВСЬКИЙ",
    "ПОЛОГІВСЬКИЙ",
    "ПОЛОНСЬКИЙ",
    "ПОЛТАВСЬКИЙ",
    "ПОЛІСЬКИЙ",
    "ПОПАСНЯНСЬКИЙ",
    "ПОПІЛЬНЯНСЬКИЙ",
    "ПРИАЗОВСЬКИЙ",
    "ПРИДНІПРОВСЬКИЙ",
    "ПРИЛУЦЬКИЙ",
    "ПРИМОРСЬКИЙ",
    "ПРОЛЕТАРСЬКИЙ",
    "ПУЛИНСЬКИЙ",
    "ПУСТОМИТІВСЬКИЙ",
    "ПУТИВЛЬСЬКИЙ",
    "ПУТИЛЬСЬКИЙ",
    "ПІВДЕННИЙ",
    "ПІВДЕННО-ЗАХІДНИЙ",
    "ПІДВОЛОЧИСЬКИЙ",
    "ПІДГАЄЦЬКИЙ",
    "ПІЩАНСЬКИЙ",
    "П’ЯТИХАТСЬКИЙ"
  ],
  "Р": [
    "РАДЕХІВСЬКИЙ",
    "РАДИВИЛІВСЬКИЙ",
    "РАДОМИШЛЬСЬКИЙ",
    "РАДЯНСЬКИЙ",
    "РАТНІВСЬКИЙ",
    "РАХІВСЬКИЙ",
    "РЕНІЙСЬКИЙ",
    "РЕШЕТИЛІВСЬКИЙ",
    "РОГАТИНСЬКИЙ",
    "РОЖИЩЕНСЬКИЙ",
    "РОЖНЯТІВСЬКИЙ",
    "РОЗДОЛЬНЕНСЬКИЙ",
    "РОЗДІЛЬНЯНСЬКИЙ",
    "РОЗІВСЬКИЙ",
    "РОКИТНЯНСЬКИЙ",
    "РОКИТНІВСЬКИЙ",
    "РОМАНІВСЬКИЙ",
    "РОМЕНСЬКИЙ",
    "РУЖИНСЬКИЙ",
    "РІВНЕНСЬКИЙ",
    "РІПКИНСЬКИЙ"
  ],
  "С": [
    "СОНЯЧНИЙ КУРОРТНИЙ",
    "САВРАНСЬКИЙ",
    "САДГІРСЬКИЙ",
    "САКСАГАНСЬКИЙ",
    "САКСЬКИЙ",
    "САМАРСЬКИЙ",
    "САМБІРСЬКИЙ",
    "САРАТСЬКИЙ",
    "САРНЕНСЬКИЙ",
    "САХНОВЩИНСЬКИЙ",
    "СВАЛЯВСЬКИЙ",
    "СВАТІВСЬКИЙ",
    "СВЕРДЛОВСЬКИЙ",
    "СВЯТОШИНСЬКИЙ",
    "СВІТЛОВОДСЬКИЙ",
    "СЕМЕНІВСЬКИЙ",
    "СЕРЕДИНО-БУДСЬКИЙ",
    "СИНЕЛЬНИКІВСЬКИЙ",
    "СИХІВСЬКИЙ",
    "СКАДОВСЬКИЙ",
    "СКВИРСЬКИЙ",
    "СКОЛІВСЬКИЙ",
    "СЛАВУТСЬКИЙ",
    "СЛОБІДСЬКИЙ",
    "СЛОВ’ЯНОСЕРБСЬКИЙ",
    "СЛОВ’ЯНСЬКИЙ",
    "СМІЛЯНСЬКИЙ",
    "СНОВСЬКИЙ",
    "СНЯТИНСЬКИЙ",
    "СНІГУРІВСЬКИЙ",
    "СОБОРНИЙ",
    "СОВЄТСЬКИЙ",
    "СОКАЛЬСЬКИЙ",
    "СОКИРЯНСЬКИЙ",
    "СОЛОМ’ЯНСЬКИЙ",
    "СОЛОНЯНСЬКИЙ",
    "СОРОКИНСЬКИЙ",
    "СОСНИЦЬКИЙ",
    "СОСНІВСЬКИЙ",
    "СОФІЇВСЬКИЙ",
    "СРІБНЯНСЬКИЙ",
    "СТАВИЩЕНСЬКИЙ",
    "СТАНИЧНО-ЛУГАНСЬКИЙ",
    "СТАРОБЕШІВСЬКИЙ",
    "СТАРОБІЛЬСЬКИЙ",
    "СТАРОВИЖІВСЬКИЙ",
    "СТАРОКИЇВСЬКИЙ",
    "СТАРОКОСТЯНТИНІВСЬКИЙ",
    "СТАРОМІСЬКИЙ",
    "СТАРОСАМБІРСЬКИЙ",
    "СТАРОСИНЯВСЬКИЙ",
    "СТОРОЖИНЕЦЬКИЙ",
    "СТРИЙСЬКИЙ",
    "СУВОРОВСЬКИЙ",
    "СУМСЬКИЙ",
    "СІМФЕРОПОЛЬСЬКИЙ"
  ],
  "Т": [
    "ТАЛАЛАЇВСЬКИЙ",
    "ТАЛЬНІВСЬКИЙ",
    "ТАРАЩАНСЬКИЙ",
    "ТАРУТИНСЬКИЙ",
    "ТАТАРБУНАРСЬКИЙ",
    "ТЕЛЬМАНІВСЬКИЙ",
    "ТЕОФІПОЛЬСЬКИЙ",
    "ТЕПЛИЦЬКИЙ",
    "ТЕРЕБОВЛЯНСЬКИЙ",
    "ТЕРНОПІЛЬСЬКИЙ",
    "ТЕРНІВСЬКИЙ",
    "ТЕТІЇВСЬКИЙ",
    "ТИВРІВСЬКИЙ",
    "ТИСМЕНИЦЬКИЙ",
    "ТЛУМАЦЬКИЙ",
    "ТОКМАЦЬКИЙ",
    "ТОМАКІВСЬКИЙ",
    "ТОМАШПІЛЬСЬКИЙ",
    "ТРОСТЯНЕЦЬКИЙ",
    "ТРОЇЦЬКИЙ",
    "ТУЛЬЧИНСЬКИЙ",
    "ТУРКІВСЬКИЙ",
    "ТУРІЙСЬКИЙ",
    "ТЯЧІВСЬКИЙ"
  ],
  "У": [
    "УЖГОРОДСЬКИЙ",
    "УЛЬЯНОВСЬКИЙ",
    "УМАНСЬКИЙ",
    "УСТИНІВСЬКИЙ"
  ],
  "Ф": [
    "ФАСТІВСЬКИЙ",
    "ФОРТЕЧНИЙ",
    "ФРАНКІВСЬКИЙ",
    "ФРУНЗЕНСЬКИЙ",
    "ФРУНЗІВСЬКИЙ"
  ],
  "Х": [
    "ХАРКІВСЬКИЙ",
    "ХМЕЛЬНИЦЬКИЙ",
    "ХМІЛЬНИЦЬКИЙ",
    "ХОЛОДНОГІРСЬКИЙ",
    "ХОРОЛЬСЬКИЙ",
    "ХОРОШІВСЬКИЙ",
    "ХОРТИЦЬКИЙ",
    "ХОТИНСЬКИЙ",
    "ХРИСТИНІВСЬКИЙ",
    "ХУСТСЬКИЙ"
  ],
  "Ц": [
    "ЦАРИЧАНСЬКИЙ",
    "ЦЕНТРАЛЬНИЙ",
    "ЦЕНТРАЛЬНО-МІСЬКИЙ",
    "ЦЮРУПИНСЬКИЙ"
  ],
  "Ч": [
    "ЧАПЛИНСЬКИЙ",
    "ЧЕМЕРОВЕЦЬКИЙ",
    "ЧЕРВОНОАРМІЙСЬКИЙ",
    "ЧЕРВОНОГВАРДІЙСЬКИЙ",
    "ЧЕРВОНОЗАВОДСЬКИЙ",
    "ЧЕРКАСЬКИЙ",
    "ЧЕРНЯХІВСЬКИЙ",
    "ЧЕРНІВЕЦЬКИЙ",
    "ЧЕРНІГІВСЬКИЙ",
    "ЧЕЧЕЛЬНИЦЬКИЙ",
    "ЧЕЧЕЛІВСЬКИЙ",
    "ЧИГИРИНСЬКИЙ",
    "ЧОРНОБАЇВСЬКИЙ",
    "ЧОРНОМОРСЬКИЙ",
    "ЧОРНУХИНСЬКИЙ",
    "ЧОРТКІВСЬКИЙ",
    "ЧУГУЇВСЬКИЙ",
    "ЧУДНІВСЬКИЙ",
    "ЧУТІВСЬКИЙ"
  ],
  "Ш": [
    "ШАРГОРОДСЬКИЙ",
    "ШАХТАРСЬКИЙ",
    "ШАЦЬКИЙ",
    "ШЕВЧЕНКІВСЬКИЙ",
    "ШЕПЕТІВСЬКИЙ",
    "ШИРОКІВСЬКИЙ",
    "ШИРЯЇВСЬКИЙ",
    "ШИШАЦЬКИЙ",
    "ШОСТКИНСЬКИЙ",
    "ШПОЛЯНСЬКИЙ",
    "ШУМСЬКИЙ"
  ],
  "Щ": [
    "ЩОРСЬКИЙ"
  ],
  "Ю": [
    "ЮР’ЇВСЬКИЙ"
  ],
  "Я": [
    "ЯВОРІВСЬКИЙ",
    "ЯГОТИНСЬКИЙ",
    "ЯКИМІВСЬКИЙ",
    "ЯМПІЛЬСЬКИЙ",
    "ЯРМОЛИНЕЦЬКИЙ",
    "ЯСИНУВАТСЬКИЙ"
  ]
}