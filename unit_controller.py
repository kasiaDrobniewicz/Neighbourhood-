from unit_view import UnitView
from unit_dao import UnitDao
from voivodeship_controller import VoivodeshipController


class UnitController():

    def __init__(self):
        self.unit_dao = UnitDao()
        self.voivodeship_controller = VoivodeshipController()

    def start(self):
        voivodeship = self.unit_dao.import_data()
        to_continue = True
        correct_choices = ["1", "2", "3", "4", "5", "6"]
        while to_continue:
            UnitView.display_collection(UnitView.MENU_OPTIONS)
            user_choice = UnitView.user_input("Enter your choice (1, 2, 3, 4, 5, 6): ")
            if user_choice not in correct_choices:
                to_continue = False
            elif user_choice == "1":
                self.voivodeship_controller.list_statistics(voivodeship)
            elif user_choice == "2":
                self.voivodeship_controller.get_cities(voivodeship)
            elif user_choice == "3":
                self.voivodeship_controller.get_county_with_largest_number_of_communities(voivodeship)
            elif user_choice == "4":
                self.voivodeship_controller.get_locations(voivodeship)
            elif user_choice == "5":
                self.voivodeship_controller.advanced_search(voivodeship)
            elif user_choice == "6":
                exit()
