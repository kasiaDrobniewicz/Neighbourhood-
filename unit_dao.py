import csv
from unit_model import Unit
from voivodeship_model import Voivodeship
from county_model import County
from community_model import Community

    
class UnitDao():

    def __init__(self):
        self.unit_collection = []

    def import_data(self):
        TYPE_IDX = 5
        NAME_IDX = 4
        VOIVODESHIP_UID_IDX = 0
        COUNTY_UID_IDX = 1
        COMMUNITY_UID_IDX = 2
        RGMI_IDX = 3
        RGMI_TYPES = ["gmina", "gmina miejska", "gmina wiejska", "gmina miejsko-wiejska", "obszar wiejski", "miasto", "delegatura"]
        COUNTY_TYPES = ["powiat", "miasto na prawach powiatu"]

        with open("malopolska.csv", "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                separated_data = line[0].strip().split("\t")
                self.unit_collection.append(separated_data)

        for unit in self.unit_collection:
            if unit[TYPE_IDX] == Voivodeship.VOIVODESHIP_TYPE:
                voivodeship = Voivodeship(unit[NAME_IDX], unit[VOIVODESHIP_UID_IDX])
            elif unit[TYPE_IDX] in COUNTY_TYPES:
                county = County(unit[NAME_IDX], unit[COUNTY_UID_IDX], unit[TYPE_IDX])
                voivodeship.add_county(county)
            elif unit[TYPE_IDX] in RGMI_TYPES:
                if unit[COMMUNITY_UID_IDX] not in voivodeship.county_dict[unit[COUNTY_UID_IDX]].community_dict.keys():
                    community = Community(unit[TYPE_IDX], unit[RGMI_IDX], unit[NAME_IDX], unit[COMMUNITY_UID_IDX])
                    voivodeship.county_dict[unit[COUNTY_UID_IDX]].add_community(community)
                else:
                    voivodeship.county_dict[unit[COUNTY_UID_IDX]].community_dict[unit[COMMUNITY_UID_IDX]].add_rgmi_type(unit[TYPE_IDX], unit[RGMI_IDX])
            else:
                pass

        return voivodeship
