import unittest
from solar_system_model.models import SpaceObject, Planet


class TestSpaceObject(unittest.TestCase):
    def setUp(self):
        self.test_object = SpaceObject("TestObject", (50, 120), (3, 4))

    def test_get_coordinates(self):
        self.assertEqual((50, 120), self.test_object.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_object.get_velocity())


class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.test_planet = Planet("TestPlanet", (50, 120), (3, 4), 1000)

    def test_get_coordinates(self):
        self.assertEqual((50, 120), self.test_planet.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_planet.get_velocity())


if __name__ == "__main__":
    unittest.main()
