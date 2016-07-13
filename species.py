class Species(object):
    def __init__(self):
        self.common_name = ""
        self.geo_region = ""

class BettaTrifasciata(Species):
    def __init__(self, color):
        self.color = color
        self.common_name = "Betta"
        self.geo_region = "Asia"
