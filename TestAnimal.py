import unittest

import animals
import species
import movement

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.swim = movement.Swimming()
        self.walk = movement.Walking()
        self.bob = animals.Betta("Bob", "orange")

    def test_animal_creation(self):
        bob = animals.Betta("Bob", "orange")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.species.color, "orange")
        self.assertIsInstance(bob, animals.Animal)
        self.assertIsInstance(bob.species, species.Species)
        self.assertIsInstance(bob.species, species.BettaTrifasciata)

    def test_locomotion_initialization(self):
        bob = animals.Betta("Bob", "orange")
        self.assertIsInstance(bob.locomotion, set)
        self.assertEqual(len(bob.locomotion), 0)

    def test_add_locomotion(self):
        self.bob = animals.Betta("Bob", "orange")
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
