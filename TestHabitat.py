import unittest

from zoolandia import *

class TestHabitat(unittest.TestCase):

    def test_name_empty_string_default(self):
        a_habitat = Habitat()
        self.assertEqual(a_habitat.name, "")

    def test_members_set_default(self):
        a_habitat = Habitat()
        self.assertIsInstance(a_habitat.members, set)

    def test_add_member(self):
        aquarium = Aquarium("freshwater")
        bob = Betta("Bob", "orange")
        james = Betta("James", "blue")
        aquarium.add_member(bob)
        aquarium.add_member(james)
        self.assertIn(bob, aquarium.members)
        self.assertIn(james, aquarium.members)

    def test_remove_member(self):
        aquarium = Aquarium("freshwater")
        bob = Betta("Bob", "orange")
        james = Betta("James", "blue")
        aquarium.add_member(bob)
        aquarium.add_member(james)
        aquarium.remove_member(james)
        self.assertIn(bob, aquarium.members)
        self.assertNotIn(james, aquarium.members)


if __name__ == "__main__":
    unittest.main()
