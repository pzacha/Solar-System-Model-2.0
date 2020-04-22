import unittest

from solar_system_model.models import SpaceObject, Spacecraft
from solar_system_model.simulation import SolarSystemSimulation


class TestSpaceObject(unittest.TestCase):
    def setUp(self):
        self.test_object = SpaceObject(1000, [2, 60], [3, 4])
        self.test_simulation = SolarSystemSimulation()
        self.celestials = {"obj": SpaceObject(10 ** 10, [-2, 63], [0, 0])}

    def test_get_coordinates(self):
        self.assertEqual([2, 60], self.test_object.get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(5, self.test_object.get_velocity())

    def test_calc_distance(self):
        self.assertEqual([-4, 3, 5], self.test_object.calc_distance([-2, 63]))

    def test_calc_force(self):
        force = [round(num, 1) for num in [-4 / 5 * 26.7, 3 / 5 * 26.7, 26.7]]
        self.assertEqual(force, [round(num, 1) for num in self.test_object.calc_force(self.celestials["obj"])])

    def test_calc_acceleration(self):
        self.assertEqual(
            [-0.021, 0.016], [round(num, 3) for num in self.test_object.calc_acceleration(self.celestials)],
        )

    def test_update_attributes(self):
        velocity = [self.test_object.velocity[0] - 0.021, self.test_object.velocity[1] + 0.016]
        position = [self.test_object.position[0] + 2.979, self.test_object.position[1] + 4.016]
        self.test_object.update_attributes(self.celestials, 1)
        self.assertEqual(velocity, [round(num, 3) for num in self.test_object.velocity])
        self.assertEqual(position, [round(num, 3) for num in self.test_object.position])


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
        planets = {}
        planets["Mercury"] = True
        planets["Venus"] = True
        planets["Earth"] = True
        planets["Mars"] = True
        planets["Jupiter"] = True
        planets["Saturn"] = True
        planets["Uranus"] = True
        planets["Neptune"] = True
        self.test_simulation.insert_celestials(planets)

    def test_celestials(self):
        self.assertEqual(SolarSystemSimulation.celestials["Sun"].mass, 1.989 * (10 ** 30))

    def test_normalize_position(self):
        self.assertEqual([153846.2, 10256410.3], self.test_simulation.normalize_position([10 ** 9, 5 * 10 ** 10]))

    def test_calc_elapsed_time(self):
        self.assertEqual("Elapsed time: 3 days", self.test_simulation.calc_elapsed_time(2500))


if __name__ == "__main__":
    unittest.main()
