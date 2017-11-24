from prettytable import PrettyTable


class UnitView(): #TBD

    def display_statistics(self, statistics, header):
        ptable = PrettyTable()
        ptable.field_names = header
        for row in statistics:
            ptable.add_row(row)
        print(ptable)