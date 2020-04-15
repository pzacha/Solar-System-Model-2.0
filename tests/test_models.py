import unittest
from solar_system_model.models import SpaceObject


class TestSpaceObject(unittest.TestCase):
    def setUp(self):
        test_object = SpaceObject("TestObject", (50, 120), (3, 4))

    def test_get_coordinates(self):
        self.assertEqual((50, 120), test_object.test_get_coordinates())

    def test_get_velocity(self):
        self.assertEqual(25, test_object.test_get_velocity())


if __name__ == "__main__":
    unittest.main()
