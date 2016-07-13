import unittest

from zoolandia import *

class TestSpecies(unittest.TestCase):

    def test_commonname_empty_string_default(self):
        a_species = Species()
        self.assertEqual(a_species.common_name, "")

    def test_georegion_emtpy_string_default(self):
        a_species = Species()
        self.assertEqual(a_species.geo_region, "")


if __name__ == "__main__":
    unittest.main()
