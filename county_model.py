from unit_model import Unit


class County(Unit):

    def __init__(self, name, uid, county_type):
        super().__init__(name, uid)
        self.county_type = county_type
        self.community_dict = {}

    def add_community(self, community):
        self.community_dict[community.uid] = community

    def __str__(self):
        return self.name

