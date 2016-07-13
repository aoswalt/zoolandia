import unittest

from zoolandia import *

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.swim = Swimming()
        self.walk = Walking()
        self.bob = Betta("Bob", "orange")

    def test_animal_creation(self):
        bob = Betta("Bob", "orange")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.species.color, "orange")
        self.assertIsInstance(bob, Animal)
        self.assertIsInstance(bob.species, Species)
        self.assertIsInstance(bob.species, BettaTrifasciata)

    def test_locomotion_initialization(self):
        bob = Betta("Bob", "orange")
        self.assertIsInstance(bob.locomotion, set)
        self.assertEqual(len(bob.locomotion), 0)

    def test_add_locomotion(self):
        self.bob = Betta("Bob", "orange")
        self.bob.add_locomotion(self.swim)
        self.assertIn(self.swim, self.bob.locomotion)


    def test_remove_locomotion(self):
        self.bob.add_locomotion(self.swim)
        self.bob.add_locomotion(self.walk)
        self.bob.remove_locomotion(self.swim)
        self.assertNotIn(self.swim, self.bob.locomotion)
        self.assertIn(self.walk, self.bob.locomotion)


if __name__ == "__main__":
    unittest.main()
