"""
AddressFormat provides methods to convert a raw address into a USPS approved 
address format.
"""

__version__ = 0.1
__author__ = "Brandon Schlueter"

import re
FULL_ADDRESS = re.compile('^[0-9]+[ ]*'
    '([NESW]?|NORTH|SOUTH|WEST|EAST|NORTHWEST|NORTHEAST|SOUTHEAST|SOUTHWEST)'
    )

STATE_TO_ABBREVIATION = {   "ALABAMA": "AL",
                            "ALASKA": "AK",
                            "AMERICAN SAMOA": "AS",
                            "ARIZONA": "AZ",
                            "ARKANSAS": "AR",
                            "Armed Forces Africa": "AE",
                            "Armed Forces Americas": "AA",
                            "Armed Forces Canada": "AE",
                            "Armed Forces Europe": "AE",
                            "Armed Forces Middle East": "AE",
                            "Armed Forces Pacific": "AP",
                            "CALIFORNIA": "CA",
                            "COLORADO": "CO",
                            "CONNECTICUT": "CT",
                            "DELAWARE": "DE",
                            "DISTRICT OF COLUMBIA": "DC",
                            "FEDERATED STATES OF MICRONESIA": "FM",
                            "FLORIDA": "FL",
                            "GEORGIA": "GA",
                            "GUAM": "GU",
                            "HAWAII": "HI",
                            "IDAHO": "ID",
                            "ILLINOIS": "IL",
                            "INDIANA": "IN",
                            "IOWA": "IA",
                            "KANSAS": "KS",
                            "KENTUCKY": "KY",
                            "LOUISIANA": "LA",
                            "MAINE": "ME",
                            "MARSHALL ISLANDS": "MH",
                            "MARYLAND": "MD",
                            "MASSACHUSETTS": "MA",
                            "MICHIGAN": "MI",
                            "MINNESOTA": "MN",
                            "MISSISSIPPI": "MS",
                            "MISSOURI": "MO",
                            "MONTANA": "MT",
                            "NEBRASKA": "NE",
                            "NEVADA": "NV",
                            "NEW HAMPSHIRE": "NH",
                            "NEW JERSEY": "NJ",
                            "NEW MEXICO": "NM",
                            "NEW YORK": "NY",
                            "NORTH CAROLINA": "NC",
                            "NORTH DAKOTA": "ND",
                            "NORTHERN MARIANA ISLANDS": "MP",
                            "OHIO": "OH",
                            "OKLAHOMA": "OK",
                            "OREGON": "OR",
                            "PALAU": "PW",
                            "PENNSYLVANIA": "PA",
                            "PUERTO RICO": "PR",
                            "RHODE ISLAND": "RI",
                            "SOUTH CAROLINA": "SC",
                            "SOUTH DAKOTA": "SD",
                            "TENNESSEE": "TN",
                            "TEXAS": "TX",
                            "UTAH": "UT",
                            "VERMONT": "VT",
                            "VIRGIN ISLANDS": "VI",
                            "VIRGINIA": "VA",
                            "WASHINGTON": "WA",
                            "WEST VIRGINIA": "WV",
                            "WISCONSIN": "WI",
                            "WYOMING": "WY",
                            "Alberta": "AB",
                            "British Columbia": "BC",
                            "Manitoba": "MB",
                            "New Brunswick": "NB",
                            "Newfoundland": "NF",
                            "Northwest Territories": "NT",
                            "Nova Scotia": "NS",
                            "Ontario": "ON",
                            "Prince Edward Island": "PE",
                            "Quebec": "QC",
                            "Saskatchewan": "SK",
                            "Yukon Territory": "YT"}

GEOGRAPHIC_DIRECTIONALS =  {"North": "N", 
                            "Northeast": "NE",
                            "East": "E",
                            "Southeast": "SE",
                            "South": "S", 
                            "Southwest": "SW",
                            "West": "W", 
                            "Northwest": "NW"}

STREET_ABBREVIATIONS = {'AVEN': 'AVE',
                        'AVNUE': 'AVE',
                        'AVENU': 'AVE',
                        'AVN': 'AVE',
                        'AV': 'AVE',
                        'AVE': 'AVE',
                        'AVENUE': 'AVE',
                        'BAYOU': 'BYU',
                        'BAYOO': 'BYU',
                        'BCH': 'BCH',
                        'BEACH': 'BCH',
                        'BEND': 'BND',
                        'BND': 'BND',
                        'BLUF': 'BLF',
                        'BLF': 'BLF',
                        'BLUFF': 'BLF',
                        'BLUFFS': 'BLFS',
                        'BTM': 'BTM',
                        'BOTTM': 'BTM',
                        'BOT': 'BTM',
                        'BOTTOM': 'BTM',
                        'BLVD': 'BLVD',
                        'BOULV': 'BLVD',
                        'BOUL': 'BLVD',
                        'BOULEVARD': 'BLVD',
                        'BRNCH': 'BR',
                        'BR': 'BR',
                        'BRANCH': 'BR',
                        'BRG': 'BRG',
                        'BRIDGE': 'BRG',
                        'BRDGE': 'BRG',
                        'BRK': 'BRK',
                        'BROOK': 'BRK',
                        'BROOKS': 'BRKS',
                        'BURG': 'BG',
                        'BURGS': 'BGS',
                        'BYPS': 'BYP',
                        'BYPA': 'BYP',
                        'BYPAS': 'BYP',
                        'BYP': 'BYP',
                        'BYPASS': 'BYP',
                        'CP': 'CP',
                        'CAMP': 'CP',
                        'CMP': 'CP',
                        'CANYON': 'CYN',
                        'CANYN': 'CYN',
                        'CNYN': 'CYN',
                        'CAPE': 'CPE',
                        'CPE': 'CPE',
                        'CSWY': 'CSWY',
                        'CAUSWA': 'CSWY',
                        'CAUSEWAY': 'CSWY',
                        'CNTER': 'CTR',
                        'CTR': 'CTR',
                        'CENTRE': 'CTR',
                        'CEN': 'CTR',
                        'CENT': 'CTR',
                        'CNTR': 'CTR',
                        'CENTR': 'CTR',
                        'CENTER': 'CTR',
                        'CENTERS': 'CTRS',
                        'CIRC': 'CIR',
                        'CRCLE': 'CIR',
                        'CIR': 'CIR',
                        'CIRCL': 'CIR',
                        'CIRCLE': 'CIR',
                        'CRCL': 'CIR',
                        'CIRCLES': 'CIRS',
                        'CLF': 'CLF',
                        'CLIFF': 'CLF',
                        'CLIFFS': 'CLFS',
                        'CLFS': 'CLFS',
                        'CLUB': 'CLB',
                        'CLB': 'CLB',
                        'COMMON': 'CMN',
                        'COMMONS': 'CMNS',
                        'CORNER': 'COR',
                        'COR': 'COR',
                        'CORNERS': 'CORS',
                        'CORS': 'CORS',
                        'COURSE': 'CRSE',
                        'CRSE': 'CRSE',
                        'COURT': 'CT',
                        'CT': 'CT',
                        'COURTS': 'CTS',
                        'CTS': 'CTS',
                        'COVE': 'CV',
                        'CV': 'CV',
                        'COVES': 'CVS',
                        'CRK': 'CRK',
                        'CREEK': 'CRK',
                        'CRSNT': 'CRES',
                        'CRES': 'CRES',
                        'CRESCENT': 'CRES',
                        'CRSENT': 'CRES',
                        'CREST': 'CRST',
                        'CROSSING': 'XING',
                        'CRSSNG': 'XING',
                        'XING': 'XING',
                        'CROSSROAD': 'XRD',
                        'CROSSROADS': 'XRDS',
                        'CURVE': 'CURV',
                        'DALE': 'DL',
                        'DL': 'DL',
                        'DAM': 'DM',
                        'DM': 'DM',
                        'DV': 'DV',
                        'DVD': 'DV',
                        'DIV': 'DV',
                        'DIVIDE': 'DV',
                        'DRIV': 'DR',
                        'DR': 'DR',
                        'DRIVE': 'DR',
                        'DRV': 'DR',
                        'DRIVES': 'DRS',
                        'EST': 'EST',
                        'ESTATE': 'EST',
                        'ESTATES': 'ESTS',
                        'ESTS': 'ESTS',
                        'EXPY': 'EXPY',
                        'EXPR': 'EXPY',
                        'EXPRESS': 'EXPY',
                        'EXPW': 'EXPY',
                        'EXP': 'EXPY',
                        'EXPRESSWAY': 'EXPY',
                        'EXTN': 'EXT',
                        'EXT': 'EXT',
                        'EXTNSN': 'EXT',
                        'EXTENSION': 'EXT',
                        'EXTS': 'EXTS',
                        'EXTENSIONS': 'EXTS',
                        'FALL': 'FALL',
                        'FLS': 'FLS',
                        'FALLS': 'FLS',
                        'FERRY': 'FRY',
                        'FRY': 'FRY',
                        'FRRY': 'FRY',
                        'FIELD': 'FLD',
                        'FLD': 'FLD',
                        'FIELDS': 'FLDS',
                        'FLDS': 'FLDS',
                        'FLAT': 'FLT',
                        'FLT': 'FLT',
                        'FLATS': 'FLTS',
                        'FLTS': 'FLTS',
                        'FRD': 'FRD',
                        'FORD': 'FRD',
                        'FORDS': 'FRDS',
                        'FRST': 'FRST',
                        'FOREST': 'FRST',
                        'FORESTS': 'FRST',
                        'FORGE': 'FRG',
                        'FRG': 'FRG',
                        'FORG': 'FRG',
                        'FORGES': 'FRGS',
                        'FORK': 'FRK',
                        'FRK': 'FRK',
                        'FORKS': 'FRKS',
                        'FRKS': 'FRKS',
                        'FRT': 'FT',
                        'FT': 'FT',
                        'FORT': 'FT',
                        'FREEWAY': 'FWY',
                        'FRWAY': 'FWY',
                        'FRWY': 'FWY',
                        'FREEWY': 'FWY',
                        'FWY': 'FWY',
                        'GARDN': 'GDN',
                        'GRDN': 'GDN',
                        'GARDEN': 'GDN',
                        'GRDEN': 'GDN',
                        'GDNS': 'GDNS',
                        'GRDNS': 'GDNS',
                        'GARDENS': 'GDNS',
                        'GTWAY': 'GTWY',
                        'GATWAY': 'GTWY',
                        'GTWY': 'GTWY',
                        'GATEWAY': 'GTWY',
                        'GATEWY': 'GTWY',
                        'GLEN': 'GLN',
                        'GLN': 'GLN',
                        'GLENS': 'GLNS',
                        'GRN': 'GRN',
                        'GREEN': 'GRN',
                        'GREENS': 'GRNS',
                        'GROVE': 'GRV',
                        'GRV': 'GRV',
                        'GROV': 'GRV',
                        'GROVES': 'GRVS',
                        'HARBOR': 'HBR',
                        'HARBR': 'HBR',
                        'HARB': 'HBR',
                        'HRBOR': 'HBR',
                        'HBR': 'HBR',
                        'HARBORS': 'HBRS',
                        'HAVEN': 'HVN',
                        'HVN': 'HVN',
                        'HTS': 'HTS',
                        'HT': 'HTS',
                        'HEIGHTS': 'HTS',
                        'HIWY': 'HWY',
                        'HIGHWAY': 'HWY',
                        'HWY': 'HWY',
                        'HWAY': 'HWY',
                        'HIWAY': 'HWY',
                        'HIGHWY': 'HWY',
                        'HILL': 'HL',
                        'HL': 'HL',
                        'HLS': 'HLS',
                        'HILLS': 'HLS',
                        'HOLW': 'HOLW',
                        'HOLWS': 'HOLW',
                        'HLLW': 'HOLW',
                        'HOLLOWS': 'HOLW',
                        'HOLLOW': 'HOLW',
                        'INLT': 'INLT',
                        'INLET': 'INLT',
                        'ISLAND': 'IS',
                        'IS': 'IS',
                        'ISLND': 'IS',
                        'ISS': 'ISS',
                        'ISLANDS': 'ISS',
                        'ISLNDS': 'ISS',
                        'ISLE': 'ISLE',
                        'ISLES': 'ISLE',
                        'JCT': 'JCT',
                        'JCTN': 'JCT',
                        'JUNCTION': 'JCT',
                        'JCTION': 'JCT',
                        'JUNCTN': 'JCT',
                        'JUNCTON': 'JCT',
                        'JCTNS': 'JCTS',
                        'JCTS': 'JCTS',
                        'JUNCTIONS': 'JCTS',
                        'KY': 'KY',
                        'KEY': 'KY',
                        'KEYS': 'KYS',
                        'KYS': 'KYS',
                        'KNL': 'KNL',
                        'KNOL': 'KNL',
                        'KNOLL': 'KNL',
                        'KNOLLS': 'KNLS',
                        'KNLS': 'KNLS',
                        'LAKE': 'LK',
                        'LK': 'LK',
                        'LAKES': 'LKS',
                        'LKS': 'LKS',
                        'LAND': 'LAND',
                        'LNDNG': 'LNDG',
                        'LNDG': 'LNDG',
                        'LANDING': 'LNDG',
                        'LN': 'LN',
                        'LANE': 'LN',
                        'LIGHT': 'LGT',
                        'LGT': 'LGT',
                        'LIGHTS': 'LGTS',
                        'LF': 'LF',
                        'LOAF': 'LF',
                        'LOCK': 'LCK',
                        'LCK': 'LCK',
                        'LOCKS': 'LCKS',
                        'LCKS': 'LCKS',
                        'LODGE': 'LDG',
                        'LDGE': 'LDG',
                        'LODG': 'LDG',
                        'LDG': 'LDG',
                        'LOOPS': 'LOOP',
                        'LOOP': 'LOOP',
                        'MALL': 'MALL',
                        'MNR': 'MNR',
                        'MANOR': 'MNR',
                        'MNRS': 'MNRS',
                        'MANORS': 'MNRS',
                        'MEADOW': 'MDW',
                        'MDWS': 'MDWS',
                        'MEADOWS': 'MDWS',
                        'MEDOWS': 'MDWS',
                        'MDW': 'MDWS',
                        'MEWS': 'MEWS',
                        'MILL': 'ML',
                        'MILLS': 'MLS',
                        'MISSN': 'MSN',
                        'MISSION': 'MSN',
                        'MSSN': 'MSN',
                        'MOTORWAY': 'MTWY',
                        'MT': 'MT',
                        'MOUNT': 'MT',
                        'MNT': 'MT',
                        'MOUNTAIN': 'MTN',
                        'MOUNTIN': 'MTN',
                        'MNTN': 'MTN',
                        'MNTAIN': 'MTN',
                        'MTN': 'MTN',
                        'MTIN': 'MTN',
                        'MOUNTAINS': 'MTNS',
                        'MNTNS': 'MTNS',
                        'NCK': 'NCK',
                        'NECK': 'NCK',
                        'ORCHRD': 'ORCH',
                        'ORCH': 'ORCH',
                        'ORCHARD': 'ORCH',
                        'OVAL': 'OVAL',
                        'OVL': 'OVAL',
                        'OVERPASS': 'OPAS',
                        'PARK': 'PARK',
                        'PRK': 'PARK',
                        'PARKS': 'PARK',
                        'PKY': 'PKWY',
                        'PARKWAY': 'PKWY',
                        'PKWY': 'PKWY',
                        'PARKWY': 'PKWY',
                        'PKWAY': 'PKWY',
                        'PARKWAYS': 'PKWY',
                        'PKWYS': 'PKWY',
                        'PASS': 'PASS',
                        'PASSAGE': 'PSGE',
                        'PATH': 'PATH',
                        'PATHS': 'PATH',
                        'PIKE': 'PIKE',
                        'PIKES': 'PIKE',
                        'PINE': 'PNE',
                        'PINES': 'PNES',
                        'PNES': 'PNES',
                        'PLACE': 'PL',
                        'PL': 'PL',
                        'PLAIN': 'PLN',
                        'PLN': 'PLN',
                        'PLAINS': 'PLNS',
                        'PLNS': 'PLNS',
                        'PLAZA': 'PLZ',
                        'PLZ': 'PLZ',
                        'PLZA': 'PLZ',
                        'PT': 'PT',
                        'POINT': 'PT',
                        'POINTS': 'PTS',
                        'PTS': 'PTS',
                        'PRT': 'PRT',
                        'PORT': 'PRT',
                        'PRTS': 'PRTS',
                        'PORTS': 'PRTS',
                        'PR': 'PR',
                        'PRAIRIE': 'PR',
                        'PRR': 'PR',
                        'RADL': 'RADL',
                        'RAD': 'RADL',
                        'RADIEL': 'RADL',
                        'RADIAL': 'RADL',
                        'RAMP': 'RAMP',
                        'RANCHES': 'RNCH',
                        'RANCH': 'RNCH',
                        'RNCH': 'RNCH',
                        'RNCHS': 'RNCH',
                        'RAPID': 'RPD',
                        'RPD': 'RPD',
                        'RPDS': 'RPDS',
                        'RAPIDS': 'RPDS',
                        'RST': 'RST',
                        'REST': 'RST',
                        'RDG': 'RDG',
                        'RIDGE': 'RDG',
                        'RDGE': 'RDG',
                        'RDGS': 'RDGS',
                        'RIDGES': 'RDGS',
                        'RIV': 'RIV',
                        'RVR': 'RIV',
                        'RIVER': 'RIV',
                        'RIVR': 'RIV',
                        'RD': 'RD',
                        'ROAD': 'RD',
                        'ROADS': 'RDS',
                        'RDS': 'RDS',
                        'ROUTE': 'RTE',
                        'ROW': 'ROW',
                        'RUE': 'RUE',
                        'RUN': 'RUN',
                        'SHL': 'SHL',
                        'SHOAL': 'SHL',
                        'SHLS': 'SHLS',
                        'SHOALS': 'SHLS',
                        'SHOAR': 'SHR',
                        'SHORE': 'SHR',
                        'SHR': 'SHR',
                        'SHORES': 'SHRS',
                        'SHOARS': 'SHRS',
                        'SHRS': 'SHRS',
                        'SKYWAY': 'SKWY',
                        'SPRING': 'SPG',
                        'SPNG': 'SPG',
                        'SPRNG': 'SPG',
                        'SPG': 'SPG',
                        'SPRINGS': 'SPGS',
                        'SPGS': 'SPGS',
                        'SPRNGS': 'SPGS',
                        'SPNGS': 'SPGS',
                        'SPUR': 'SPUR',
                        'SPURS': 'SPUR',
                        'SQR': 'SQ',
                        'SQ': 'SQ',
                        'SQUARE': 'SQ',
                        'SQU': 'SQ',
                        'SQRE': 'SQ',
                        'SQRS': 'SQS',
                        'SQUARES': 'SQS',
                        'STATN': 'STA',
                        'STN': 'STA',
                        'STATION': 'STA',
                        'STA': 'STA',
                        'STRAV': 'STRA',
                        'STRAVEN': 'STRA',
                        'STRAVN': 'STRA',
                        'STRVN': 'STRA',
                        'STRAVENUE': 'STRA',
                        'STRVNUE': 'STRA',
                        'STRA': 'STRA',
                        'STREME': 'STRM',
                        'STRM': 'STRM',
                        'STREAM': 'STRM',
                        'STREET': 'ST',
                        'ST': 'ST',
                        'STR': 'ST',
                        'STRT': 'ST',
                        'STREETS': 'STS',
                        'SMT': 'SMT',
                        'SUMMIT': 'SMT',
                        'SUMITT': 'SMT',
                        'SUMIT': 'SMT',
                        'TER': 'TER',
                        'TERRACE': 'TER',
                        'TERR': 'TER',
                        'THROUGHWAY': 'TRWY',
                        'TRCE': 'TRCE',
                        'TRACES': 'TRCE',
                        'TRACE': 'TRCE',
                        'TRACK': 'TRAK',
                        'TRACKS': 'TRAK',
                        'TRKS': 'TRAK',
                        'TRK': 'TRAK',
                        'TRAK': 'TRAK',
                        'TRAFFICWAY': 'TRFY',
                        'TRLS': 'TRL',
                        'TRAIL': 'TRL',
                        'TRL': 'TRL',
                        'TRAILS': 'TRL',
                        'TRLR': 'TRLR',
                        'TRLRS': 'TRLR',
                        'TRAILER': 'TRLR',
                        'TUNEL': 'TUNL',
                        'TUNNEL': 'TUNL',
                        'TUNLS': 'TUNL',
                        'TUNL': 'TUNL',
                        'TUNNL': 'TUNL',
                        'TUNNELS': 'TUNL',
                        'TURNPIKE': 'TPKE',
                        'TURNPK': 'TPKE',
                        'TRNPK': 'TPKE',
                        'UNDERPASS': 'UPAS',
                        'UNION': 'UN',
                        'UN': 'UN',
                        'UNIONS': 'UNS',
                        'VLY': 'VLY',
                        'VALLEY': 'VLY',
                        'VALLY': 'VLY',
                        'VLLY': 'VLY',
                        'VALLEYS': 'VLYS',
                        'VLYS': 'VLYS',
                        'VIADUCT': 'VIA',
                        'VDCT': 'VIA',
                        'VIA': 'VIA',
                        'VIADCT': 'VIA',
                        'VW': 'VW',
                        'VIEW': 'VW',
                        'VWS': 'VWS',
                        'VIEWS': 'VWS',
                        'VILLAG': 'VLG',
                        'VILLG': 'VLG',
                        'VILLIAGE': 'VLG',
                        'VLG': 'VLG',
                        'VILL': 'VLG',
                        'VILLAGE': 'VLG',
                        'VLGS': 'VLGS',
                        'VILLAGES': 'VLGS',
                        'VILLE': 'VL',
                        'VL': 'VL',
                        'VSTA': 'VIS',
                        'VIS': 'VIS',
                        'VISTA': 'VIS',
                        'VST': 'VIS',
                        'VIST': 'VIS',
                        'WALK': 'WALK',
                        'WALKS': 'WALK',
                        'WALL': 'WALL',
                        'WY': 'WAY',
                        'WAY': 'WAY',
                        'WAYS': 'WAYS',
                        'WELL': 'WL',
                        'WLS': 'WLS',
                        'WELLS': 'WLS'}

SECONDARY_UNIT_DESIGNATORS = {"Apartment": "APT",
                              "Basement": "BSMT",
                              "Building": "BLDG",
                              "Department": "DEPT",
                              "Floor": "FL",
                              "Front": "FRNT",
                              "Hanger": "HNGR",
                              "Key": "KEY",
                              "Lobby": "LBBY",
                              "Lot": "LOT",
                              "Lower": "LOWR",
                              "Office": "OFC",
                              "Penthouse": "PH",
                              "Pier": "PIER",
                              "Rear": "REAR",
                              "Room": "RM",
                              "Side": "SIDE",
                              "Slip": "SLIP",
                              "Space": "SPC",
                              "Stop": "STOP",
                              "Suite": "STE",
                              "Trailer": "TRLR",
                              "Unit": "UNIT",
                              "Upper": "UPPR"}


def standardize(address, delimiter = "", error_level = 0):
    '''Takes an address in string form as an argument and returns 
    a revised address in USPS standard format. The delimiter is 
    the character which lies between the street and city portions 
    of the address. If none is provided, both a comma and a line 
    return are tested. If the address cannot be broken down, a 
    ValueError is raised.'''
    pass
#    if :
#    else :
#        throw PyException(Py.ValueError, "Unable to parse address from "+address)
    
def breakdown(address, delimiter = ""):
    pass
def delivery_address_standardize(address):
    '''Takes the first line of an address containing the primary 
    address number, predirectional, street name, suffix, 
    postdirectional, secondary address indentifier, and secondary 
    address as a single space delimited string formatted like: 
    '101 W MAIN ST S APT 12'.  
    Only the primary address number and  street name are required.
    Returns a string in USPS approved format.'''
    
    address = address.rsplit(' ')
    address_number = address[0]
    if +   

def last_line_standardize(last_line, divider = "", error_level = 0):
    '''Takes the last line of an address containing the city, 
    state and zip with an optional divider or a space between 
    city and state and spaces between state and zip and 
    returns a USPS approved last line.'''
    city,state,zip = '','',''
    if divider:
         city,state = last_line.rsplit(divider)
         state,zip = state.strip().rsplit(" ")
    else:
        last_line = last_line.rsplit(" ")
        # assumes that the last two elements delimited by spaces are the state
        # and zip, and that everything before is the city.
        city,state,zip = last_line[:-2][0],last_line[-2],last_line[-1] 
    #check zip
    if not( zip[:5].isnumeric() and (len(zip) == 5 or (len(zip) == 10 and 
            zip[5] == '-' and zip[6:].isnumeric()))):
        if error_level == 0:
            print "WARNING: Bad zip code:",zip
        elif error_level == 1:
            raise ValueError, "Bad zip code: "+zip
        else:
            print "WARNING: Bad zip code:",zip
    
    city,state = city.upper(),state.upper()
    
    #check and abbreviate state
    if len(state) > 2:
        try:
            state = STATE_TO_ABBREVIATION[state]
        except KeyError:
            if error_level == 0:
                print "WARNING: Unrecognized state:",state
            elif error_level == 1:
                raise ValueError, "Unrecognized state: "+state
            else:
                print "WARNING: Unrecognized state:",state
    else:
        if STATE_TO_ABBREVIATION.keys().count(state) == 0:
            if error_level == 0:
                print "WARNING: Unrecognized state:",state
            elif error_level == 1:
                raise ValueError, "Unrecognized state: "+state
            else:
                print "WARNING: Unrecognized state:",state
    return city+' '+state+' '+zip
    
            
            
        