class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species



class Species(object):
    def __init__(self):
        self.common_name = ""
        self.geo_region = ""

class BettaTrifasciata(Species):
    def __init__(self, color):
        self.color = color
        self.common_name = "Betta"
        self.geo_region = "Asia"


class Habitat(object):
    def __init__(self):
        self.name = ""
        self.members = set()

    def add_member(self, animal):
        self.members.add(animal)

    def remove_member(self, animal):
        self.members.discard(animal)


class Aquarium(Habitat):
    def __init__(self, water_type):
        Habitat.__init__(self)
        self.water_type = water_type



class Walking(object):
    def __init__(self):
        self.legs = 0
        self.walk_speed = 0


class Swimming(object):
    def __init__(self):
        self.fins = False
        self.flippers = False
        self.web_feet = False
        self.swim_speed = 0

class Flying(object):
    def __init__(self):
        self.wings = 0
        self.air_speed = 0
        self.wingspan = 0


class Betta(Animal, Swimming):
    def __init__(self, name, color):
        Animal.__init__(self, name, BettaTrifasciata(color))
