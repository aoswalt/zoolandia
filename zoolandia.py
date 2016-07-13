from animals import *
from species import *
from movement import *
from habitat import *

if __name__ == "__main__":
    swim = Swimming()
    bob = Betta("Bob", "blue")
    bob.add_locomotion(swim)
    betty = Betta("Betty", "black")
    bob.add_locomotion(swim)

    print(bob)
    print(betty)
