from species import *
from movement import *

class Animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.locomotion = set()

    def add_locomotion(self, loco):
        self.locomotion.add(loco)

    def remove_locomotion(self, loco):
        self.locomotion.remove(loco)

    def locomotion_string(self):
        return "".join([str(l) + ", " for l in self.locomotion])[:-2]

    def __str__(self):
        return "{} the {} {}".format(self.name,
                                     self.locomotion_string(),
                                     self.species.common_name)

class Betta(Animal):
    def __init__(self, name, color):
        super().__init__(name, BettaTrifasciata(color))

    def __str__(self):
        return "{} the {} {} {}".format(self.name,
                                        self.locomotion_string(),
                                        self.species.color,
                                        self.species.common_name)
