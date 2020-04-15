import numpy as np


class Object:
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

    def __init__(self, name, position, velocity):
        self.name = name
        self.position = position
        self.velocity = velocity

    def get_coordinates(self):
        return self.position

    def get_velocity(self):
        v_x, v_y = self.velocity
        return np.sqrt(v_x ** 2 + v_y ** 2)
