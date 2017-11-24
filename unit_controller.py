import sys
import os
from unit_view import UnitView
from unit_dao import UnitDao
from voivodeship_model import Voivodeship
from county_model import County
from community_model import Community


class UnitController():

    MENU_OPTIONS = ["List statistics",
                    "Display 3 cities with longest names",
                    "Display county's name with the largest number of communities",
                    "Display locations, that belong to more than one category",
                    "Advanced search",
                    "Exit program"]

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
        
        #self.unit_view.display_statistics(list_stats, ["", "MAŁOPOLSKA"])
        
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

    """def get_cities(self, voivodeship):
        cities_dict = {}
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "miasto" in community.rgmi_dict.values():
                    #cities_dict = {}
                    key_name = community.name
                    value_len_name = str(len(community.name))
                    #print(type(value_len_name))
                    #cities_dict[community.name] = str(len(community.name))
                    cities_dict.update({key_name: value_len_name})
                    print(cities_dict)
                    #print(cities_dict)
                    #print(list(cities_dict.values()))
                    #values = cities_dict.values()
                    #print(values)
                    #longest_cities = 0
        longest_cities = 0            
        for key in cities_dict:
            print(key)
            print(cities_dict[key])
            if int(cities_dict[key]) > longest_cities:
                longest_cities = int(cities_dict[key])
                #print(longest_cities)
                        #print(key)
                        #longest_cities = 0

                            #cities_dict[key] = key
                    #print(key)
                            #print(len(community))"""

    def get_cities(self, voivodeship):
        cities_dict = {}
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "miasto" in community.rgmi_dict.values():
                    key_name = community.name
                    value_len_name = str(len(community.name))
                    cities_dict.update({key_name: value_len_name})
        cities_len = list(cities_dict.items()) 
        longest_cities = 0            
        for key in cities_dict:
            if int(cities_dict[key]) > longest_cities:
                longest_cities = int(cities_dict[key])
        print(longest_cities)
        print(key)

    def display_menu(self):
        self.view.display_menu(self.MENU_OPTIONS)

    def start(self):
        to_continue = True
        correct_choices = ["1", "2", "3", "4", "5", "6"]
        while to_continue:
            UnitView.display_menu(self.MENU_OPTIONS)
            user_choice = self.unit_view.user_input("Enter your choice (1, 2, 3, 4, 5, 6): ")
            os.system("clear")
            if user_choice not in correct_choices:
                to_continue = False
            elif user_choice == "1":
                list_stats = unit_controller.list_statistics(voivodeship)
                self.unit_view.display_statistics(list_stats, ["", "MAŁOPOLSKA"])
            elif user_choice == "2":
                pass
            elif user_choice == "3":
                pass
            elif user_choice == "4":
                pass
            elif user_choice == "5":
                pass
            elif user_choice == "6":
                exit()


unit_dao = UnitDao()
voivodeship = unit_dao.import_data()
unit_controller = UnitController()
#unit_controller.start()
#unit_controller.list_statistics(voivodeship)
unit_controller.count_rgmis(voivodeship)
unit_controller.get_cities(voivodeship)

#UnitView.display_menu(UnitController.MENU_OPTIONS)
