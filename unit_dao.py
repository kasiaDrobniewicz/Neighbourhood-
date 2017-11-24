import csv
from unit_model import Unit
from voivodeship_model import Voivodeship
from county_model import County
from community_model import Community

    
class UnitDao():

    def __init__(self):
        self.unit_collection = self.import_data()

