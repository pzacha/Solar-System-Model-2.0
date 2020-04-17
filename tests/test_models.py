import unittest

from solar_system_model.models import SpaceObject, Spacecraft, SolarSystemSimulation


class TestSpaceObject(unittest.TestCase):
    def setUp(self):
        self.test_object = SpaceObject(1000, [2, 60], [3, 4])
        self.test_simulation = SolarSystemSimulation()

    def test_get_coordinates(self):
        self.assertEqual([2, 60], self.test_object.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_object.get_velocity())

    def test_calc_distance(self):
        self.assertEqual([-4, 3, 5], self.test_object.calc_distance([-2, 63]))

    def test_calc_force(self):
        test_object2 = SpaceObject(1000, [-2, 63], [0, 0])
        force = [round(num, 8) for num in [-4 / 5 * 2.67e-06, 3 / 5 * 2.67e-06, 2.67e-06]]
        self.assertEqual(force, [round(num, 8) for num in self.test_object.calc_force(test_object2)])

    def test_calc_acceleration(self):
        self.assertEqual(
            [-1227082627631963.0, -3.681247882895889e16],
            self.test_object.calc_acceleration(SolarSystemSimulation.celestials),
        )


class TestSpacecraft(unittest.TestCase):
    def setUp(self):
        self.test_spacecraft = Spacecraft(100, [50, 120], [3, 4], 100)

    def test_get_coordinates(self):
        self.assertEqual([50, 120], self.test_spacecraft.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_spacecraft.get_velocity())


class TestSolarSystemSimulation(unittest.TestCase):
    def setUp(self):
        self.test_simulation = SolarSystemSimulation()

    def test_celestials(self):
        self.assertEqual(len(SolarSystemSimulation.celestials), 5)
        self.assertEqual(SolarSystemSimulation.celestials["Sun"].mass, 1.989 * (10 ** 30))


if __name__ == "__main__":
    unittest.main()
