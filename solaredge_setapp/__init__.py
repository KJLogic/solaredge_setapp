from solaredge_setapp import app_configs
from solaredge_setapp import communication
from solaredge_setapp import device_manager
from solaredge_setapp import information
from solaredge_setapp import maintenance
from solaredge_setapp import power_control
from solaredge_setapp import grid_protection
from solaredge_setapp import region
from solaredge_setapp import status

import enum
import itertools


_COUNTRIES = {
    -1: ["Not Set", "COUNTRY_NONE"],
    0: ["General", "COUNTRY_GENERAL"],
    1: ["Australia", "COUNTRY_AUSTRALIA"],
    2: ["France", "COUNTRY_FRANCE"],
    3: ["Germany", "COUNTRY_GERMANY"],
    4: ["Greece (Continent)", "COUNTRY_GREECE_CONTINENT"],
    5: ["Greece (Islands)", "COUNTRY_GREECE_ISLANDS"],
    6: ["Israel", "COUNTRY_ISRAEL"],
    7: ["Italy", "COUNTRY_ITALY"],
    8: ["Spain", "COUNTRY_SPAIN"],
    9: ["United Kingdom", "COUNTRY_UK"],
    10: ["US Auto", "COUNTRY_US_AUTO"],
    11: ["US 208V", "COUNTRY_US_208V"],
    12: ["US 240V", "COUNTRY_US_240V"],
    13: ["US 208V No-Neutral", "COUNTRY_US_208V_NO_NEUTRAL"],
    14: ["US 240V No-Neutral", "COUNTRY_US_240V_NO_NEUTRAL"],
    15: ["Bulgaria", "COUNTRY_BULGARIA"],
    16: ["Czech Republic", "COUNTRY_CZECH_REPUBLIC"],
    17: ["Cyprus", "COUNTRY_CYPRESS"],
    18: ["Belgium", "COUNTRY_BELGIUM"],
    19: ["Netherlands", "COUNTRY_NETHERLANDS"],
    20: ["Portugal", "COUNTRY_PORTUGAL"],
    21: ["Austria", "COUNTRY_AUSTRIA"],
    22: ["Thailand MEA", "COUNTRY_THAILAND_MEA"],
    23: ["Singapore", "COUNTRY_SINGAPORE"],
    24: ["Korea", "COUNTRY_KOREA"],
    25: ["Japan Auto", "COUNTRY_JAPAN_AUTO"],
    26: ["Japan 50Hz", "COUNTRY_JAPAN_50HZ"],
    27: ["Japan 60Hz", "COUNTRY_JAPAN_60HZ"],
    28: ["Taiwan", "COUNTRY_TAIWAN"],
    29: ["Denmark", "COUNTRY_DENMARK"],
    30: ["Sweden", "COUNTRY_SWEDEN"],
    31: ["Thailand PEA", "COUNTRY_THAILAND_PEA"],
    32: ["Sri Lanka", "COUNTRY_SRI_LANKA"],
    33: ["Mauritius", "COUNTRY_MAURITIUS"],
    34: ["Denmark (Residential)", "COUNTRY_DENMARK_RES"],
    35: ["US 277V", "COUNTRY_US_277V"],
    36: ["Slovenia", "COUNTRY_SLOVENIA"],
    37: ["Poland", "COUNTRY_POLAND"],
    38: ["Germany MVGC", "COUNTRY_GERMANY_MVGC"],
    39: ["UK 240V", "COUNTRY_UK_240V"],
    40: ["Lithuania", "COUNTRY_LITHUANIA"],
    41: ["China", "COUNTRY_CHINA"],
    42: ["Philipines", "COUNTRY_PHILIPPINES"],
    43: ["Brazil", "COUNTRY_BRAZIL"],
    44: ["Mexico 220V", "COUNTRY_MEXICO_220"],
    45: ["Mexico 277V", "COUNTRY_MEXICO_277"],
    46: ["Romania", "COUNTRY_ROMANIA"],
    47: ["Latvia", "COUNTRY_LATVIA"],
    48: ["South Africa", "COUNTRY_SOUTH_AFRICA"],
    49: ["Turkey", "COUNTRY_TURKEY"],
    50: ["Italy No SPI", "COUNTRY_ITALY_NO_SPI"],
    51: ["US/Hawaii Auto", "COUNTRY_US_HAWAII_AUTO"],
    52: ["US/Hawaii 208V", "COUNTRY_US_HAWAII_208V"],
    53: ["US/Hawaii 240V", "COUNTRY_US_HAWAII_240V"],
    54: ["US/Hawaii 208V No-Neutral", "COUNTRY_US_HAWAII_208V_NO_NEUTRAL"],
    55: ["US/Hawaii 240V No-Neutral", "COUNTRY_US_HAWAII_240V_NO_NEUTRAL"],
    56: ["US/Hawaii 277V", "COUNTRY_US_HAWAII_277"],
    57: ["Switzerland", "COUNTRY_SWITZERLAND"],
    58: ["Custom", "COUNTRY_CUSTOM"],
    59: ["India", "COUNTRY_INDIA"],
    60: ["Croatia", "COUNTRY_CROATIA"],
    61: ["Jamaica 240V No-Neutral", "COUNTRY_JAMAICA_240_NO_NEUTRAL"],
    62: ["Jamaica 220V No-Neutral", "COUNTRY_JAMAICA_220_NO_NEUTRAL"],
    63: ["Barbados 230V No-Neutral", "COUNTRY_BARBADOS_230_NO_NEUTRAL"],
    64: ["St. Lucia", "COUNTRY_ST_LUCIA"],
    65: ["Australia Queensland", "COUNTRY_AUSTRALIA_QLD"],
    66: ["Denmark VDE", "COUNTRY_DENMARK_VDE"],
    67: ["Denmark VDE (Residential)", "COUNTRY_DENMARK_VDE_RES"],
    68: ["Ireland", "COUNTRY_IRELAND"],
    69: ["US/Kauai Auto", "COUNTRY_US_KAUAI_AUTO"],
    70: ["US/Kauai 208V", "COUNTRY_US_KAUAI_208"],
    71: ["US/Kauai 240V", "COUNTRY_US_KAUAI_240"],
    72: ["US/Kauai 208V No-Neutral", "COUNTRY_US_KAUAI_208_NO_NEUTRAL"],
    73: ["US/Kauai 240V No-Neutral", "COUNTRY_US_KAUAI_240_NO_NEUTRAL"],
    74: ["US/Kauai 277V", "COUNTRY_US_KAUAI_277"],
    75: ["Cyprus 240V", "COUNTRY_CYPRESS_240"],
    76: ["Curacao", "COUNTRY_CURACAO"],
    77: ["Northern Cyprus 240V", "COUNTRY_N_CYPRESS_240"],
    78: ["Israel (Commercial)", "COUNTRY_ISRAEL_COMMERCIAL"],
    79: ["Aruba", "COUNTRY_ARUBA"],
    80: ["Mexico 240V", "COUNTRY_MEXICO_240"],
    81: ["Barbados 115V No-Neutral", "COUNTRY_BARBADOS_115V_NO_NEUTRAL"],
    82: ["Malaysia", "COUNTRY_MALAYSIA"],
    83: ["Tahiti", "COUNTRY_TAHITI"],
    84: ["Hungary", "COUNTRY_HUNGARY"],
    85: ["Kuwait", "COUNTRY_KUWAIT"],
    86: ["Cyprus MV", "COUNTRY_CYPRUS_MV"],
    87: ["Norway", "COUNTRY_NORWAY"],
    88: ["Northern Ireland", "COUNTRY_NORTH_IRELAND"],
    89: ["Germany MV 480V", "COUNTRY_GERMANY_MV_480V"],
    90: ["US/Hawaii2 Auto", "COUNTRY_US_HAWAII2_AUTO"],
    91: ["US/Hawaii2 208V", "COUNTRY_US_HAWAII2_208V"],
    92: ["US/Hawaii2 240V", "COUNTRY_US_HAWAII2_208V_NO_NEUTRAL"],
    93: ["US/Hawaii2 208V No-Neutral", "COUNTRY_US_HAWAII2_240V"],
    94: ["US/Hawaii2 240V No-Neutral", "COUNTRY_US_HAWAII2_240V_NO_NEUTRAL"],
    95: ["US/Hawaii2 277V", "COUNTRY_US_HAWAII2_277"],
    96: ["US/NY Auto", "COUNTRY_US_NY_AUTO"],
    97: ["US/NY 208V", "COUNTRY_US_NY_208V"],
    98: ["US/NY 240V ", "COUNTRY_US_NY_208V_NO_NEUTRAL"],
    99: ["US/NY 208V No-Neutral", "COUNTRY_US_NY_240V"],
    100: ["US/NY 240V No-Neutral", "COUNTRY_US_NY_240V_NO_NEUTRAL"],
    101: ["US/NY 277V ", "COUNTRY_US_NY_277"],
    102: ["Japan MV 420V 50Hz", "COUNTRY_JAPAN_MV_380V_50HZ"],
    103: ["Japan MV 440V 60Hz", "COUNTRY_JAPAN_MV_380V_60HZ"],
    104: ["US/Rule21 Auto", "COUNTRY_US_AUTO_RULE21"],
    105: ["US/Rule21 208V", "COUNTRY_US_208V_RULE21"],
    106: ["US/Rule21 208V No-Neutral", "COUNTRY_US_208V_NO_NEUTRAL_RULE21"],
    107: ["US/Rule21 240V", "COUNTRY_US_240V_RULE21"],
    108: ["US/Rule21 240V No-Neutral", "COUNTRY_US_240V_NO_NEUTRAL_RULE21"],
    109: ["US/Rule21 277V", "COUNTRY_US_277V_RULE21"],
    110: ["Italy 277V No SPI", "COUNTRY_ITALY_277V_NO_SPI"],
    111: ["Philippines 230V Delta", "COUNTRY_PHILIPPINES_230V_DELTA"],
    112: ["UK 480V", "COUNTRY_UK_480V"],
    113: ["Zimbabwe 230V", "COUNTRY_ZIMBABWE_230V"],
    114: ["Indonesia", "COUNTRY_INDONESIA"],
    115: ["Japan MV 480V 50Hz", "COUNTRY_JAPAN_MV_480V_50_HZ"],
    116: ["Japan MV 480V 60Hz", "COUNTRY_JAPAN_MV_480V_60_HZ"],
    117: ["Europe EN50438", "COUNTRY_EUROPE_EN50438"],
    118: ["Cape Verde", "COUNTRY_CAPE_VERDE"],
    119: ["New Zealand", "COUNTRY_NEW_ZEALAND"],
    120: ["Ghana", "COUNTRY_GHANA"],
    121: ["Finland", "COUNTRY_FINLAND"],
    122: ["Grenada", "COUNTRY_GRENADA"],
    123: ["Dubai LV", "COUNTRY_DUBAI_LV"],
    124: ["Slovakia ZSED", "COUNTRY_SLOVAKIA_ZSED"],
    125: ["Slovakia SSED", "COUNTRY_SLOVAKIA_SSED"],
    126: ["Slovakia VSD", "COUNTRY_SLOVAKIA_VSD"],
    127: ["Puerto Rico 277V", "COUNTRY_PUERTO_RICO_277V"],
    128: ["South Africa MV", "COUNTRY_SOUTH_AFRICA_MV"],
    129: ["Philippines MV", "COUNTRY_PHILIPPINES_MV"],
    130: ["Taiwan MV", "COUNTRY_TAIWAN_MV"],
    131: ["India MV", "COUNTRY_INDIA_MV"],
    132: ["US/CO Auto", "COUNTRY_US_CO_AUTO"],
    133: ["US/CO 208V", "COUNTRY_US_CO_208V"],
    134: ["US/CO 208V No-Neutral", "COUNTRY_US_CO_208V_NO_NEUTRAL"],
    135: ["US/CO 240V No-Neutral", "COUNTRY_US_CO_240V_NO_NEUTRAL"],
    136: ["US/CO 240V", "COUNTRY_US_CO_240V"],
    137: ["US/CO 277V", "COUNTRY_US_CO_277V"],
    138: ["Australia Victoria", "COUNTRY_VICTORIA"],
    139: ["Kenya", "COUNTRY_KENYA"],
    140: ["Turkey MV", "COUNTRY_TURKEY_MV"],
    141: ["Spain MV", "COUNTRY_SPAIN_MV"],
    142: ["Thailand MEA MV", "COUNTRY_THAILAND_MEA_MV"],
    143: ["Thailand PEA MV", "COUNTRY_THAILAND_PEA_MV"],
    144: ["China MV", "COUNTRY_CHINA_MV"],
    145: ["Taiwan 220V No-Neutral", "COUNTRY_TAIWAN_220_NO_NEUTRAL"],
    146: ["Mauritius >220K", "COUNTRY_MAURITIUS_ABOVE_220K"],
    147: ["France MV", "COUNTRY_FRANCE_MV"],
    148: ["Czech Republic 16A", "COUNTRY_CEZ"],
    149: ["Belgium Delta", "COUNTRY_BELGIUM_DELTA"],
    150: ["Norway Delta", "COUNTRY_NORWAY_DELTA"],
    151: ["Netherlands MV", "COUNTRY_NETHERLANDS_MV"],
    152: ["Macau", "COUNTRY_MACAU"],
    153: ["Argentina", "COUNTRY_ARGENTINA"],
    154: ["Argentina (Commercial)", "COUNTRY_ARGENTINA_COMMERCIAL"],
    155: ["Sweden MV", "COUNTRY_SWEDEN_MV"],
    156: ["Vietnam", "COUNTRY_VIETNAM"],
    157: ["Brzail 127V-220V", "COUNTRY_BRAZIL_127V_220V"],
    158: ["Barbados 220V", "COUNTRY_BARBADOS_200"],
    159: ["ISO-NE 208V", "COUNTRY_US_NEW_ENGLAND_208"],
    160: ["ISO-NE 240V", "COUNTRY_US_NEW_ENGLAND_240"],
    161: ["ISO-NE 208V No-Neutral", "COUNTRY_US_NEW_ENGLAND_208_NO_NEUTRAL"],
    162: ["ISO-NE 240V No-Neutral", "COUNTRY_US_NEW_ENGLAND_240_NO_NEUTRAL"],
    163: ["ISO-NE 277V", "COUNTRY_US_NEW_ENGLAND_277"],
    164: ["Korea Low DC", "COUNTRY_KOREA_LOW_DC"],
    165: ["Israel 480 MV", "COUNTRY_ISRAEL_480V_MV"],
    166: ["Brzail 277V", "COUNTRY_BRAZIL_277"],
    167: ["Hungary EON", "COUNTRY_HUNGARY_EON"],
    168: ["Spain (Islands)", "COUNTRY_SPANISH_ISLANDS"],
    169: ["Peru", "COUNTRY_PERU"],
    170: ["Columbia", "COUNTRY_COLUMBIA"],
    171: ["Chile", "COUNTRY_CHILE"],
    172: ["Ecuador", "COUNTRY_ECUADOR"],
    173: ["Qatar", "COUNTRY_QATAR"],
    174: ["Australia 480V", "COUNTRY_AUSTRALIA_480V"],
    175: ["Hong Kong", "COUNTRY_HONG_KONG"],
    176: ["Uruguay", "COUNTRY_URUGUAY"],
    177: ["Italy A68", "COUNTRY_ITALIY_A68"],
    178: ["Estonia", "COUNTRY_ESTONIA"]
}
Countries = enum.Enum(
    value="Countries",
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _COUNTRIES.items()
    )
)


_LANGUAGES = {
    0: ["English", "ENGLISH"],
    1: ["German", "GERMAN"],
    2: ["Spanish (Hispanic)", "SPANISH_MEXICAN"],
    3: ["French", "FRENCH"],
    4: ["Italian", "ITALIAN"],
    5: ["Dutch", "DUTCH"],
    6: ["Japanese", "JAPANESE"],
    7: ["Korean", "KOREAN"],
    8: ["Chinese (Traditional)", "CHINESE_TRADITIONAL"],
    9: ["Portuguese (Brazilian)", "PORTUGUESE_BRAZILIAN"],
    10: ["Polish", "POLISH"],
    11: ["Hungarian", "HUNGARIAN"]
}
Languages = enum.Enum(
    value="Languages",
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _LANGUAGES.items()
    )
)


_STATUS = {
    -1: ["Not Set", "UNSET"],
    0: ["Shutting Down", "SHUTTING_DOWN"],
    1: ["Error", "ERROR"],
    2: ["Standby", "STANDBY"],
    3: ["Pairing", "PAIRING"],
    4: ["Producing", "POWER_PRODUCTION"],
    5: ["AC Charging", "AC_CHARGING"],
    6: ["Not Paired", "NOT_PAIRED"],
    7: ["Night Mode", "NIGHT_MODE"],
    8: ["Grid Monitoring", "GRID_MONITORING"],
    9: ["Idle", "IDLE"],
    10: ["Grid Pairing", "GRM_PAIRING"]
}
Status = enum.Enum(
    value="Status",
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _STATUS.items()
    )
)

_WIFI_STATUS = {
    0: ["None", "NONE"],
    1: ["Connected", "CONNECTED"],
    2: ["In Progress", "IN_PROGRESS"],
    3: ["Disconnected", "DISCONNECTED"],
    4: ["WPS Discovery", "WPS_DISCOVERY"],
    5: ["Invalid Password", "ERROR_PASSWORD"],
    6: ["DHCP Error", "ERROR_DHCP"],
    7: ["Connection Error", "ERROR_COMMUNICATION"],
    8: ["Unknown Error", "ERROR_OTHER"],
    9: ["Server Unreachable", "ERROR_UNREACHABLE"]
}
WifiStatus = enum.Enum(
    value="WifiStatus",
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _WIFI_STATUS.items()
    )
)

_WIFI_SIGNAL = {
    0: ["None", "NONE"],
    1: ["Poor", "LOW"],
    2: ["Medium", "MID"],
    3: ["Good", "HIGH"],
    4: ["Excellent", "EXCELLENT"]
}
WifiSignal = enum.Enum(
    value="WifiSignal",
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _WIFI_SIGNAL.items()
    )
)