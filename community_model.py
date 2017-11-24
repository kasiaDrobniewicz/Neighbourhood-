from unit_model import Unit


class Community(Unit):

    def __init__(self, type_rgmi, idx_rgmi, name, uid):
        super().__init__(name, uid)
        self.rgmi_dict = {idx_rgmi: type_rgmi}

    def add_rgmi_type(self, type_rgmi, idx_rgmi):
        self.rgmi_dict[idx_rgmi] = type_rgmi

    def __str__(self):
        return self.name