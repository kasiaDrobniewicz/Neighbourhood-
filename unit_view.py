class UnitView():

    MENU_OPTIONS = ["List statistics",
                    "Display 3 cities with longest names",
                    "Display county's name with the largest number of communities",
                    "Display locations, that belong to more than one category",
                    "Advanced search",
                    "Exit program"]

    SEPARATOR = "-------------------------"

    @staticmethod
    def display_collection(collection):
        for number, element in enumerate(collection):
            print(number + 1, element)

    @staticmethod
    def user_input(text=''):
        user_input = input(text)
        return user_input
