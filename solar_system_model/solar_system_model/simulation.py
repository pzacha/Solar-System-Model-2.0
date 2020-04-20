import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from solar_system_model.models import SpaceObject, Spacecraft


class SolarSystemSimulation:
    """
    A class to handle simulation.

    Attributes:
    ----------
    celestials : dict
        Class attribute. Dictionary containing celestial objects.
    timestamp : int
        Simulation timestamp value in seconds.
    """

    celestials = {}

    def __init__(self, timestamp=100):
        self.timestamp = timestamp

        # Initialize celestial objects
        sun = SpaceObject(mass=1.989 * (10 ** 30), position=[0, 0], velocity=[0, 0])
        mercury = SpaceObject(mass=0.33 * (10 ** 24), position=[-57.9 * (10 ** 9), 0], velocity=[0, -47400])
        venus = SpaceObject(mass=4.87 * (10 ** 24), position=[0, 108.2 * (10 ** 9)], velocity=[-35000, 0])
        earth = SpaceObject(mass=5.972 * (10 ** 24), position=[0, -149.6 * (10 ** 9)], velocity=[29800, 0])
        mars = SpaceObject(mass=0.642 * (10 ** 24), position=[227.9 * (10 ** 9), 0], velocity=[0, 24100])

        # Insert celestial objects into dictionary
        SolarSystemSimulation.celestials = {
            "Sun": sun,
            "Mercury": mercury,
            "Venus": venus,
            "Earth": earth,
            "Mars": mars,
        }

    def simulate_step(self):
        """Iterate through celestials and update their attributes.
        """

        for celestial in SolarSystemSimulation.celestials.items():
            celestial[1].update_attributes(SolarSystemSimulation.celestials, self.timestamp)

    def normalize_position(self, position, new_range=100, old_range=2.5 * 10 ** 11):
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

    def update_animation_data(self, x_coords, y_coords, sun_x, sun_y):
        """Updates coordinates for animation

        Parameters
        ----------
        x_coords, y_coords : list[int]
            Lists that store coordinates of planets.
        sun_x, sun_y : list[int]
            Coordinates that stores x and y coordinates of Sun.
        """

        iter = 0
        for celestial in SolarSystemSimulation.celestials.items():
            if celestial[0] != "Sun":
                x_coords[iter], y_coords[iter] = self.normalize_position(celestial[1].position)
                iter += 1
            else:
                sun_x[0], sun_y[0] = self.normalize_position(celestial[1].position)

    def calc_elapsed_time(self, frame):
        """Calculates elapsed time based on frame number and timestamp value.

        Parameters
        ----------
        frame : int
            Frame number.

        Returns
        -------
        elapsed_time : str
            Elapsed time in days.
        """

        time = frame * self.timestamp / 86400
        elapsed_time = "Elapsed time: " + str(round(time)) + " days"
        return elapsed_time

    def animation(self):
        """Starts and animates the simulation.
        """

        # Create lists for planets and sun coordinates
        planets_x = np.zeros(len(SolarSystemSimulation.celestials) - 1, dtype=int)
        planets_y = np.zeros(len(SolarSystemSimulation.celestials) - 1, dtype=int)
        sun_x = [0]
        sun_y = [0]

        # Initialize matplotlib Figure.
        fig = plt.figure(figsize=(6.4, 6.4))
        ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
        (planets,) = ax.plot([0], [0], "bo")
        (sun,) = ax.plot([0], [0], "yo")
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)

        # Defines text that displays elapsed time in days
        time_text = ax.text(0.65, 0.97, "", horizontalalignment="left", verticalalignment="top", transform=ax.transAxes)

        # Function that defines animation used in FuncAnimation class.
        def animate(i):
            self.simulate_step()
            self.update_animation_data(planets_x, planets_y, sun_x, sun_y)
            planets.set_data(planets_x, planets_y)
            sun.set_data(sun_x, sun_y)
            time_text.set_text(self.calc_elapsed_time(i))

            return (planets, sun, time_text)

        anim = FuncAnimation(fig, animate, interval=1, blit=True, repeat=False)
        # Save animation as a gif.
        # anim.save("simulation.gif", writer="imagemagick")
        plt.show()
