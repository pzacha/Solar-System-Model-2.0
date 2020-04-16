import numpy as np


class SpaceObject:
    """
    A class used to represent an solar system object.

    Attributes:
    ----------
    position : List[int]
        List that stores objects x and y coordinates in m.
    velocity : List[int]
        List that stores objects x and y components of velocity in m/s.
    """

    def __init__(self, position: List[int], velocity: List[int]):
        self.position = position
        self.velocity = velocity

    def get_coordinates(self):
        """Returns x and y coordinates of an object.

        Returns
        -------
            Position: List[int]
        """

        return self.position

    def get_velocity(self):
        """Returns x and y components of velocity.

        Returns
        -------
            Velocity: List[int]
        """

        v_x, v_y = self.velocity
        return np.sqrt(v_x ** 2 + v_y ** 2)

    def calc_distance(self, position):
        """Calculates the distance between self and position.

        Parameters
        ----------
        position : List[int]
            List that stores objects x and y coordinates in m.

        Returns
        -------
            
        """

        pass

    def calc_force(self, celestial):
        """Calculates the gravitational force between self and celestial.

        Parameters
        ----------
        celestial : CelestialObject

        Returns
        -------
            
        """

        pass

    def calc_acceleration(self, celestials):
        """Calculates acceleration by summing gravitational force from all celestials on self.

        Parameters
        ----------
        celestials : Dict
            Dict that stores all celestial objects.

        Returns
        -------
            
        """

        sum_force = [0, 0]
        for celestial in celestials:
            if self is not celestial:
                force = self.calc_force(celestial)
                sum_force[0] += force[0]
                sum_force[1] += force[1]
        return [sum_force[0] / self.mass, sum_force[1] / self.mass]

    def update_position(self):
        """Updates position attribute.
        """

        pass

    def update_velocity(self):
        """Updates velocity attribute.            
        """

        pass

    def update_attributes(self, celestials):
        """Updates self attributes.

        Parameters
        ----------
        celestials : Dict
            Dict that stores all celestial objects.            
        """

        pass


class CelestialObject(SpaceObject):
    """
    A class used to represent an solar system planet. It inherits the functionality from SpaceObject class.

    Attributes:
    ----------
    mass : int
        Mass of an object in kg.
    """

    def __init__(self, mass: int, position: List[int], velocity: List[int]):
        super().__init__(position, velocity)
        self.mass = mass


class SolarSystemSimulation:
    """
    A class to handle simulation.

    Attributes:
    ----------
    celestials : dict
        Class attribute. Dictionary containing celestial objects.
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
