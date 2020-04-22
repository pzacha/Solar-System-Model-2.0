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
    max_dist : int
        Farthest displayed position.
    ax_lim : int
        Axes limit. It corresponds to max_dist on the plot.
    screen_ratio : int
        Animation screen ratio.
    """

    celestials = {}

    def __init__(self, timestamp=100):
        self.timestamp = timestamp
        self.max_dist = 1 * 10 ** 11
        self.ax_lim = 10 ** 6
        self.screen_ratio = 4 / 3

        # Initialize celestial objects
        self.sun = SpaceObject(mass=1.989 * (10 ** 30), position=[0, 0], velocity=[0, 0])

        # Inner planets
        self.mercury = SpaceObject(mass=0.33 * (10 ** 24), position=[-57.9 * (10 ** 9), 0], velocity=[0, -47400])
        self.venus = SpaceObject(mass=4.87 * (10 ** 24), position=[0, 108.2 * (10 ** 9)], velocity=[-35000, 0])
        self.earth = SpaceObject(mass=5.972 * (10 ** 24), position=[0, -149.6 * (10 ** 9)], velocity=[29800, 0])
        self.mars = SpaceObject(mass=0.642 * (10 ** 24), position=[227.9 * (10 ** 9), 0], velocity=[0, 24100])

        # Outer planets
        self.jupiter = SpaceObject(mass=1898 * (10 ** 24), position=[-778.6 * (10 ** 9), 0], velocity=[0, -13100])
        self.saturn = SpaceObject(mass=568 * (10 ** 24), position=[0, 1433.5 * (10 ** 9)], velocity=[-9700, 0])
        self.uranus = SpaceObject(mass=86.8 * (10 ** 24), position=[0, -2872.5 * (10 ** 9)], velocity=[6800, 0])
        self.neptune = SpaceObject(mass=102 * (10 ** 24), position=[4495.1 * (10 ** 9), 0], velocity=[0, 5400])

    def insert_celestials(self, planets):
        """Insert celestial objects into dictionary. Sets max_dist attribute.

        Parameters
        ----------
        planets : list[int]
            List with planets that will be used in simulation.
        """

        SolarSystemSimulation.celestials = {
            "Sun": self.sun,
        }
        if planets["Mercury"] == True:
            SolarSystemSimulation.celestials["Mercury"] = self.mercury
            self.max_dist = 1 * 10 ** 11
        if planets["Venus"] == True:
            SolarSystemSimulation.celestials["Venus"] = self.venus
            self.max_dist = 1.6 * 10 ** 11
        if planets["Earth"] == True:
            SolarSystemSimulation.celestials["Earth"] = self.earth
            self.max_dist = 2.2 * 10 ** 11
        if planets["Mars"] == True:
            SolarSystemSimulation.celestials["Mars"] = self.mars
            self.max_dist = 3.3 * 10 ** 11
        if planets["Jupiter"] == True:
            SolarSystemSimulation.celestials["Jupiter"] = self.jupiter
            self.max_dist = 1.2 * 10 ** 12
        if planets["Saturn"] == True:
            SolarSystemSimulation.celestials["Saturn"] = self.saturn
            self.max_dist = 2.2 * 10 ** 12
        if planets["Uranus"] == True:
            SolarSystemSimulation.celestials["Uranus"] = self.uranus
            self.max_dist = 4.5 * 10 ** 12
        if planets["Neptune"] == True:
            SolarSystemSimulation.celestials["Neptune"] = self.neptune
            self.max_dist = 6.5 * 10 ** 12

    def simulate_step(self):
        """Iterate through celestials and update their attributes.
        """

        for celestial in SolarSystemSimulation.celestials.items():
            celestial[1].update_attributes(SolarSystemSimulation.celestials, self.timestamp)

    def normalize_position(self, position):
        """Normalizes position values for proper display.

        Parameters
        ----------
        position : list[int]
            List that stores position of object.

        Returns
        -------
        normalized_position : list[int]
            New normalized position. Contains x and y components.
        """

        normalized_position = [0, 0]
        normalized_position[0] = round(position[0] * self.ax_lim / self.max_dist, 1)
        normalized_position[1] = round(position[1] * self.ax_lim / self.max_dist * self.screen_ratio, 1)
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
        fig = plt.figure(figsize=(10, 7.5))
        ax = plt.axes(xlim=(-self.ax_lim, self.ax_lim), ylim=(-self.ax_lim, self.ax_lim))
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
