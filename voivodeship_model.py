from unit_model import Unit


class Voivodeship(Unit):

    def __init__(self, name, uid):
        super().__init__(name, uid)
        self.county_dict = {}

    def add_county(self, county):
        self.county_dict[county.uid] = county

    def __str__(self):
        return self.name