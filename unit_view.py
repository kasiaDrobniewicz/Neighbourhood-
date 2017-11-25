from prettytable import PrettyTable


class UnitView():  # TBD

    @staticmethod
    def display_statistics(statistics, header):
        ptable = PrettyTable()
        ptable.field_names = header
        for row in statistics:
            ptable.add_row(row)
        print(ptable)

    @staticmethod
    def display_collection(collection):
        for number, element in enumerate(collection):
            print(number + 1, element)

    @staticmethod
    def user_input(text=''):
        user_input = input(text)
        return user_input

    @staticmethod
    def display_text(text=''):
        print(text)