import unittest

from solar_system_model.models import SpaceObject, CelestialObject, SolarSystemSimulation


class TestSpaceObject(unittest.TestCase):
    def setUp(self):
        self.test_object = SpaceObject((50, 120), (3, 4))

    def test_get_coordinates(self):
        self.assertEqual((50, 120), self.test_object.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_object.get_velocity())


class TestCelestialObject(unittest.TestCase):
    def setUp(self):
        self.test_planet = CelestialObject(1000, (50, 120), (3, 4))

    def test_get_coordinates(self):
        self.assertEqual((50, 120), self.test_planet.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_planet.get_velocity())


class TestSolarSystemSimulation(unittest.TestCase):
    def setUp(self):
        self.test_simulation = SolarSystemSimulation()

    def test_celestials(self):
        self.assertEqual(len(SolarSystemSimulation.celestials), 5)
        self.assertEqual(SolarSystemSimulation.celestials["Sun"].mass, 1.989 * (10 ** 30))


if __name__ == "__main__":
    unittest.main()
