from animals import *
from species import *
from movement import *
from habitat import *

if __name__ == "__main__":
    swim = Swimming()
    walk = Walking()
    bob = Betta("Bob", "blue")
    bob.add_locomotion(swim)
    bob.add_locomotion(walk)
    betty = Betta("Betty", "black")
    betty.add_locomotion(swim)

    print(bob)
    print(betty)
