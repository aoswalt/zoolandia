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

class Betta(Animal):
    def __init__(self, name, color):
        super().__init__(name, BettaTrifasciata(color))
