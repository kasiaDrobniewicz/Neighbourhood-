import csv
from unit_model import Unit
from voivodeship_model import Voivodeship
from county_model import County
from community_model import Community

    
class UnitDao():

    def __init__(self):
        self.unit_collection = self.import_data()

    def import_data(self):
        unit_collection = []
        type_idx = 5
        name_idx = 4
        voivodeship_uid_idx = 0
        county_uid_idx = 1
        community_uid_idx = 2
        idx_rgmi = 3
        rgmi_types = ["gmina", "gmina miejska", "gmina wiejska", "gmina miejsko-wiejska", "obszar wiejski", "miasto", "delegatura"]
        county_types = ["powiat", "miasto na prawach powiatu"]
        test_number_rgmi = 0

        with open("malopolska.csv", "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                separated_data = line[0].strip().split("\t")
                unit_collection.append(separated_data)

        for unit in unit_collection:
            if unit[type_idx] == "województwo":
                voivodeship = Voivodeship(unit[name_idx], unit[voivodeship_uid_idx])
                #print("dodalam województwo")
                test_number_rgmi += 1
            elif unit[type_idx] in county_types:
                county = County(unit[name_idx], unit[county_uid_idx], unit[type_idx])
                voivodeship.add_county(county)
                #print("dodalam powiat lub miasto na prawach powiatu")
                test_number_rgmi += 1
            elif unit[type_idx] in rgmi_types:
                if unit[community_uid_idx] not in voivodeship.county_dict[unit[county_uid_idx]].community_dict.keys():
                    #print("nie ma takiej gminy więc tworzę")
                    community = Community(unit[type_idx], unit[idx_rgmi], unit[name_idx], unit[community_uid_idx])
                    voivodeship.county_dict[unit[county_uid_idx]].add_community(community)
                    test_number_rgmi += 1
                else:
                    #print("jest już taka gmina, więc dodaje tylko typ")
                    voivodeship.county_dict[unit[county_uid_idx]].community_dict[unit[community_uid_idx]].add_rgmi_type(unit[type_idx], unit[idx_rgmi])
                    test_number_rgmi += 1
            else:
                pass  
        #print(test_number_rgmi)
        return voivodeship


unit_dao = UnitDao()
voivodeship = unit_dao.import_data()

#print("Województwa: --------------------------------")
#print(voivodeship)
#print("Powiaty: --------------------------------")
#for county_key, county_value in voivodeship.county_dict.items():
#    print(county_key + " " + county_value.name)
#print("Gminy: --------------------------------")
#for county_key, county_value in voivodeship.county_dict.items():
#    for community_key, community_value in county_value.community_dict.items():
#        print(community_key + " " + community_value.name)

