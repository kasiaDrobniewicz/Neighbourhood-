from prettytable import PrettyTable


class UnitView():  # TBD

    def display_statistics(self, statistics, header):
        ptable = PrettyTable()
        ptable.field_names = header
        for row in statistics:
            ptable.add_row(row)
        print(ptable)

    @staticmethod
    def display_collection(collection):
        for number, element in enumerate(collection):
            print(number + 1, element)

    def user_input(self, text=''):
        user_input = input(text)
        return user_input

    @staticmethod
    def display_text(text=''):
        print(text)