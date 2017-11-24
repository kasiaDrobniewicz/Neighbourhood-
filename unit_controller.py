from unit_view import UnitView
from unit_dao import UnitDao
from voivodeship_model import Voivodeship
from county_model import County
from community_model import Community


class UnitController():

    def __init__(self):
        self.unit_dao = UnitDao()
        self.unit_view = UnitView()



