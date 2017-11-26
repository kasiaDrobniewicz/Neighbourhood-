from county_model import County
from community_model import Community
from voivodeship_view import VoivodeshipView


class VoivodeshipController():

    def list_statistics(self, voivodeship):
        NUMBER_OF_VOIVODESHIPS = 1
        HEADER = ["", "MAŁOPOLSKA"]
        number_of_city_counties = self.count_counties(voivodeship.county_dict, "miasto na prawach powiatu")
        number_of_counties = self.count_counties(voivodeship.county_dict, "powiat") + number_of_city_counties
        number_of_gmina_miejska, number_of_gmina_wiejska, number_of_gmina_miejsko_wiejska, number_of_obszar_wiejski, number_of_miasto, number_of_delegatura = self.count_rgmis(voivodeship)
        list_stats = []
        list_stats.append([str(NUMBER_OF_VOIVODESHIPS), "województwo"])
        list_stats.append([str(number_of_counties), "powiaty"])
        list_stats.append([str(number_of_gmina_miejska), "gmina miejska"])
        list_stats.append([str(number_of_gmina_wiejska), "gmina wiejska"])
        list_stats.append([str(number_of_gmina_miejsko_wiejska), "gmina miejsko-wiejska"])
        list_stats.append([str(number_of_obszar_wiejski), "obszar wiejski"])
        list_stats.append([str(number_of_miasto), "miasto"])
        list_stats.append([str(number_of_city_counties), "miasto na prawach powiatu"])
        list_stats.append([str(number_of_delegatura), "delegatura"])

        VoivodeshipView.display_statistics(list_stats, HEADER)

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

        return gmina_miejska_counter, gmina_wiejska_counter, gmina_miejsko_wiejska_counter, obszar_wiejski_counter, miasto_counter, delegatura_counter

    def get_cities(self, voivodeship):
        cities_list = []
        longest_cities_list = []
        NUMBER_OF_LONGEST_CITIES = 3
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if "miasto" in community.rgmi_dict.values():
                    cities_list.append(community.name)
        
        for i in range(0, NUMBER_OF_LONGEST_CITIES):
            longest_city_len = 0
            longest_city = ""
            for city in cities_list:
                if len(city) > longest_city_len:
                    longest_city_len = len(city)
                    longest_city = city
            longest_cities_list.append(longest_city)
            cities_list.remove(longest_city)

        VoivodeshipView.display_text("Three longest cities are:")
        VoivodeshipView.display_collection(longest_cities_list)
        VoivodeshipView.display_text(VoivodeshipView.SEPARATOR)

    def get_county_with_largest_number_of_communities(self, voivodeship):
        number_of_communities = 0
        county_with_largest_number_of_communities = ""
        for county_key, county in voivodeship.county_dict.items():
            if len(county.community_dict.items()) > number_of_communities:
                county_with_largest_number_of_communities = county.name
                number_of_communities = len(county.community_dict.items())

        VoivodeshipView.display_text("County with the largest number of communities is:")
        VoivodeshipView.display_text(county_with_largest_number_of_communities)
        VoivodeshipView.display_text(VoivodeshipView.SEPARATOR)

    def get_locations(self, voivodeship):
        locations = []
        for county_key, county in voivodeship.county_dict.items():
            for community_key, community in county.community_dict.items():
                if len(community.rgmi_dict.keys()) > 1:
                    locations.append(community.name)

        VoivodeshipView.display_text("Locations that belong to more than one category are:")
        VoivodeshipView.display_collection(locations)
        VoivodeshipView.display_text(VoivodeshipView.SEPARATOR)

    def advanced_search(self, voivodeship):
        HEADER = ["LOCATION", "TYPE"]
        search_results = []
        search_string = VoivodeshipView.user_input("Searching for: ")
        if search_string in voivodeship.name:
            search_results.append([voivodeship.name, Voivodeship.VOIVODESHIP_TYPE])
        for county_key, county in voivodeship.county_dict.items():
            if search_string in county.name:
                search_results.append([county.name, county.county_type])
            for community_key, community in county.community_dict.items():
                if search_string in community.name:
                    for rgmi_key, rgmi_type in community.rgmi_dict.items():
                        search_results.append([community.name, rgmi_type])
        search_results.sort(key=lambda tup: tup[1])
        search_results.sort(key=lambda tup: tup[0])

        VoivodeshipView.display_statistics(search_results, HEADER)
