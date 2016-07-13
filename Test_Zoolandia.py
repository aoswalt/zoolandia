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
import zoolandia

class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_animal_creation(self):
        bob = zoolandia.Betta("Bob", "orange")
        self.assertEqual(bob.name, "Bob")
        self.assertEqual(bob.species.color, "orange")
        self.assertIsInstance(bob, zoolandia.Animal)
        self.assertIsInstance(bob.species, zoolandia.Species)
        self.assertIsInstance(bob.species, zoolandia.BettaTrifasciata)


class TestSpecies(unittest.TestCase):

    def test_commonname_empty_string_default(self):
        a_species = zoolandia.Species()
        self.assertEqual(a_species.common_name, "")

    def test_georegion_emtpy_string_default(self):
        a_species = zoolandia.Species()
        self.assertEqual(a_species.geo_region, "")


class TestHabitat(unittest.TestCase):

    def test_name_empty_string_default(self):
        a_habitat = zoolandia.Habitat()
        self.assertEqual(a_habitat.name, "")

    def test_members_set_default(self):
        a_habitat = zoolandia.Habitat()
        self.assertIsInstance(a_habitat.members, set)

    def test_add_member(self):
        aquarium = zoolandia.Aquarium("freshwater")
        bob = zoolandia.Betta("Bob", "orange")
        james = zoolandia.Betta("James", "blue")
        aquarium.add_member(bob)
        aquarium.add_member(james)
        self.assertIn(bob, aquarium.members)
        self.assertIn(james, aquarium.members)

    def test_remove_member(self):
        aquarium = zoolandia.Aquarium("freshwater")
        bob = zoolandia.Betta("Bob", "orange")
        james = zoolandia.Betta("James", "blue")
        aquarium.add_member(bob)
        aquarium.add_member(james)
        aquarium.remove_member(james)
        self.assertIn(bob, aquarium.members)
        self.assertNotIn(james, aquarium.members)



class TestWalking(unittest.TestCase):

    def test_legs_zero_default(self):
        walking = zoolandia.Walking()
        self.assertEqual(walking.legs, 0)

    def test_walk_speed_zero_default(self):
        walking = zoolandia.Walking()
        self.assertEqual(walking.walk_speed, 0)


class TestSwimming(unittest.TestCase):

    def test_appendages_false_default(self):
        swimming = zoolandia.Swimming()
        self.assertFalse(swimming.fins)
        self.assertFalse(swimming.flippers)
        self.assertFalse(swimming.web_feet)

    def test_swim_speed_zero_default(self):
        swimming = zoolandia.Swimming()
        self.assertEqual(swimming.swim_speed, 0)


class TestFlying(unittest.TestCase):

    def test_wings_false_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wings, 0)

    def test_air_speed_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.air_speed, 0)

    def test_wingspan_zero_default(self):
        flying = zoolandia.Flying()
        self.assertEqual(flying.wingspan, 0)


if __name__ == "__main__":
    unittest.main()
