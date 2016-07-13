import unittest

from zoolandia import *

class TestWalking(unittest.TestCase):

    def test_legs_zero_default(self):
        walking = Walking()
        self.assertEqual(walking.legs, 0)

    def test_walk_speed_zero_default(self):
        walking = Walking()
        self.assertEqual(walking.walk_speed, 0)


class TestSwimming(unittest.TestCase):

    def test_appendages_false_default(self):
        swimming = Swimming()
        self.assertFalse(swimming.fins)
        self.assertFalse(swimming.flippers)
        self.assertFalse(swimming.web_feet)

    def test_swim_speed_zero_default(self):
        swimming = Swimming()
        self.assertEqual(swimming.swim_speed, 0)


class TestFlying(unittest.TestCase):

    def test_wings_false_default(self):
        flying = Flying()
        self.assertEqual(flying.wings, 0)

    def test_air_speed_zero_default(self):
        flying = Flying()
        self.assertEqual(flying.air_speed, 0)

    def test_wingspan_zero_default(self):
        flying = Flying()
        self.assertEqual(flying.wingspan, 0)


if __name__ == "__main__":
    unittest.main()
