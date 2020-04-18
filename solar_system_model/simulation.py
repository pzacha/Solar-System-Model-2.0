import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from .models import SpaceObject, Spacecraft


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
        sun = SpaceObject(mass=1.989 * (10 ** 30), position=[0, 0], velocity=[0, 0])
        # mercury = SpaceObject(mass=0.33 * (10 ** 24), position=[57.9 * (10 ** 9), 0], velocity=[47400, 0])
        # venus = SpaceObject(mass=4.87 * (10 ** 24), position=[108.2 * (10 ** 9), 0], velocity=[35000, 0])
        earth = SpaceObject(mass=5.972 * (10 ** 24), position=[149.6 * (10 ** 9), 0], velocity=[29800, 0])
        # mars = SpaceObject(mass=0.642 * (10 ** 24), position=[227.9 * (10 ** 9), 0], velocity=[24100, 0])

        # Insert celestial objects into dictionary
        SolarSystemSimulation.celestials = {
            "Sun": sun,
            # "Mercury": mercury,
            # "Venus": venus,
            "Earth": earth,
            # "Mars": mars,
        }

    # def simulate(self):

    #     for celestial in celestials.items():
    #         celestial[1].update_attributes(celestials, 100)

    def normalize_position(self, position, new_range=100, old_range=2 * 10 ** 12):
        """Normalizes position values for proper display.

        Parameters
        ----------
        position : list[int]
            List that stores position of object.
        new_range : int
            New max range.
        old_range : int
            Old max range - farthest possible position for object.

        Returns
        -------
        normalized_position : list[int]
            New normalized position. Contains x and y components.
        """

        normalized_position = [0, 0]
        normalized_position[0] = round(position[0] * new_range / old_range, 1)
        normalized_position[1] = round(position[1] * new_range / old_range, 1)
        return normalized_position

    def animation(self):
        x_cor = [0]
        y_cor = [0]

        fig = plt.figure()
        ax = plt.axes(xlim=(0, 1000), ylim=(0, 100))
        line = None
        (line,) = ax.plot([0], [0], "go")

        def animate(i):
            x_cor[0] = 2 * i
            y_cor[0] = i
            line.set_data(x_cor, y_cor)
            return (line,)

        anim = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
        plt.show()


# sim = SolarSystemSimulation()

# sim.animation()
