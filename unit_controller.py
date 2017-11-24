from unit_view import UnitView
from unit_dao import UnitDao
from voivodeship_model import Voivodeship
from county_model import County
from community_model import Community


class UnitController():

    def __init__(self):
        self.unit_dao = UnitDao()
        self.unit_view = UnitView()

    def list_statistics(self, voivodeship):
        NUMBER_OF_VOIVODESHIPS = 1
        number_of_city_counties = self.count_counties(voivodeship.county_dict, "miasto na prawach powiatu")
        number_of_counties = self.count_counties(voivodeship.county_dict, "powiat") + number_of_city_counties
        number_of_gmina_miejska, number_of_gmina_wiejska, number_of_gmina_miejsko_wiejska, number_of_obszar_wiejski, number_of_miasto, number_of_delegatura = self.count_rgmis(voivodeship)
        list_stats = []
        #list_stats.append(["MAŁOPOLSKIE"])
        list_stats.append([str(NUMBER_OF_VOIVODESHIPS), "województwo"])
        list_stats.append([str(number_of_counties), "powiaty"])
        list_stats.append([str(number_of_gmina_miejska), "gmina miejska"])
        list_stats.append([str(number_of_gmina_wiejska), "gmina wiejska"])
        list_stats.append([str(number_of_gmina_miejsko_wiejska), "gmina miejsko-wiejska"])
        list_stats.append([str(number_of_obszar_wiejski), "obszar wiejski"])
        list_stats.append([str(number_of_miasto), "miasto"])
        list_stats.append([str(number_of_city_counties), "miasto na prawach powiatu"])
        list_stats.append([str(number_of_delegatura), "delegatura"])
        
        self.unit_view.display_statistics(list_stats, ["", "MAŁOPOLSKA"])
        
        return list_stats
        '''print(str(NUMBER_OF_VOIVODESHIPS) + " | wojewódźtwo")
        print(str(number_of_counties) + " | powiaty")
        print(str(number_of_city_counties) + " | miasto na prawach powiatu ")'''
        
    def count_counties(self, county_dict, county_type):
        county_counter = 0
        for key, value in county_dict.items():
            if county_type == value.county_type:
                county_counter += 1
        return county_counter

    def count_rgmis(self, voivodeship):
        gmina_miejska_counter = 0
        gmina_wiejska_counter = 0
        gmina_miejsko_wiejska_counter = 0
        obszar_wiejski_counter = 0
        miasto_counter = 0
        delegatura_counter = 0

        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "gmina miejska" in community.rgmi_dict.values():
                    gmina_miejska_counter += 1
                if "gmina wiejska" in community.rgmi_dict.values():
                    gmina_wiejska_counter += 1
                if "gmina miejsko-wiejska" in community.rgmi_dict.values():
                    gmina_miejsko_wiejska_counter += 1
                if "obszar wiejski" in community.rgmi_dict.values():
                    obszar_wiejski_counter += 1
                if "miasto" in community.rgmi_dict.values():
                    miasto_counter += 1
                if "delegatura" in community.rgmi_dict.values():
                    delegatura_counter += 1

        '''print("gmina_miejska_counter: " + str(gmina_miejska_counter))
        print("gmina_wiejska_counter: " + str(gmina_wiejska_counter))
        print("gmina_miejsko_wiejska_counter: " + str(gmina_miejsko_wiejska_counter))
        print("obszar_wiejski_counter: " + str(obszar_wiejski_counter))
        print("miasto_counter: " + str(miasto_counter))
        print("delegatura_counter: " + str(delegatura_counter))'''

        return gmina_miejska_counter, gmina_wiejska_counter, gmina_miejsko_wiejska_counter, obszar_wiejski_counter, miasto_counter, delegatura_counter

    """def get_cities(self, voivodeship):
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "miasto" in community.rgmi_dict.values():
                    #print(community.name + " " + (str(len(community.name))))
                    #print(list(len(communit))
                    return (str(len(community.name)))"""

    def get_cities(self, voivodeship):
        cities_dict = {}
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "miasto" in community.rgmi_dict.values():
                    #cities_dict = {}
                    key_name = community.name
                    value_len_name = str(len(community.name))
                    #print(value_len_name)
                    #cities_dict[community.name] = str(len(community.name))
                    cities_dict.update({key_name: value_len_name})
                    #print(cities_dict)
                    #print(list(cities_dict.values()))
                    #values = cities_dict.values()
                    #print(values)
                    #longest_cities = 0
        longest_cities = 0            
        for key in cities_dict:
            #print(key)
            #longest_cities = 0
            if int(cities_dict[key]) > longest_cities:
                longest_cities = int(cities_dict[key])
                community = key
                print(key)
                #print(community.name)


    """def get_cities(self, voivodeship):
        cities_dict = {}
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "miasto" in community.rgmi_dict.values():
                    #cities_dict = {}
                    key_name = community.name
                    value_len_name = str(len(community.name))
                    cities_dict.update({key_name: value_len_name})
                    #print(cities_dict)
                    #print(list(cities_dict.values()))
        cities_len = cities_dict.items()             
        print(cities_len)
        for city in cities_len:
            max_len_city = cities_len[0]
        print(max_len_city)"""        


  



unit_dao = UnitDao()
voivodeship = unit_dao.import_data()
unit_controller = UnitController()
unit_controller.list_statistics(voivodeship)
unit_controller.count_rgmis(voivodeship)
unit_controller.get_cities(voivodeship)
#unit_controller.get_longest_cities_names(unit_controller.get_cities(voivodeship))