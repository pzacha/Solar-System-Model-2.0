import numpy as np


class SpaceObject:
    """
    A class used to represent an solar system object

    Attributes:
    ----------
    position : tuple
        tuple that stores objects x and y coordinates
    velocity : tuple
        tuple that stores objects x and y components of velocity
    name : str
        the name of an object
    Methods
    -------
    get_coordinates
        Gets x and y coordinates of an object
    get_velocity
        Gets x and y components of velocity
    """

    def __init__(self, position: tuple, velocity: tuple):
        self.position = position
        self.velocity = velocity

    def get_coordinates(self):
        return self.position

    def get_velocity(self):
        v_x, v_y = self.velocity
        return np.sqrt(v_x ** 2 + v_y ** 2)


class CelestialObject(SpaceObject):
    """
    A class used to represent an solar system planet. It inherits the functionality from SpaceObject class.

    Attributes:
    ----------
    mass : str
        the name of an object
    """

    def __init__(self, mass: int, position: tuple, velocity: tuple):
        super().__init__(position, velocity)
        self.mass = mass


class SolarSystemSimulation:
    """
    A class to handle simulation.

    Attributes:
    ----------
    celestials : dict
        class attribute. Dictionary containg celestial objects
    """

    celestials = {}

    def __init__(self):

        # Initialize celestial objects
        sun = CelestialObject(mass=1.989 * (10 ** 30), position=(0, 0), velocity=(0, 0))
        mercury = CelestialObject(mass=0.33 * (10 ** 24), position=(57.9 * (10 ** 9), 0), velocity=(47400, 0))
        venus = CelestialObject(mass=4.87 * (10 ** 24), position=(108.2 * (10 ** 9), 0), velocity=(35000, 0))
        earth = CelestialObject(mass=5.972 * (10 ** 24), position=(149.6 * (10 ** 9), 0), velocity=(29800, 0))
        mars = CelestialObject(mass=0.642 * (10 ** 24), position=(227.9 * (10 ** 9), 0), velocity=(24100, 0))

        # Insert celestial objects into dictionary
        SolarSystemSimulation.celestials = {
            "Sun": sun,
            "Mercury": mercury,
            "Venus": venus,
            "Earth": earth,
            "Mars": mars,
        }
