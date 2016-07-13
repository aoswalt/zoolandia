''' Zoolandia
To build a zoo, we need to start with the following MVP features.
1. A base Animal class.
3. A class definition for 8 animals that will be the initial exhibits of the zoo. Each one derives from the base Animal class.
5. Each animal will be designated as a walking, flying, or swimming animal by inheriting from the appropriate class.

2. A base Species class.
6. The species of an animal will be composed into the specific animal instance.
4. A class definition for the species of our 8 animals, which derive from the base Species class.

7. A base Habitat class.
8. A class definition for each habitat we need in our zoo to hold our initial 8 animals.
9. Each habitat will hold at least one animal, as an aggregation.
'''

import unittest

from TestAnimal import *
from TestSpecies import *
from TestMovement import *
from TestHabitat import *

if __name__ == "__main__":
    unittest.main()
