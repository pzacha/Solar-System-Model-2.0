import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class SpaceObject:
    """
    A class used to represent an solar system object.

    Attributes:
    ----------
    GRAV_CONST : int
        Class attribute. Gravitational constant.
    position : list[int]
        List that stores objects x and y coordinates in m.
    velocity : list[int]
        List that stores objects x and y components of velocity in m/s.
    mass : int
        Mass of an object in kg.
    """

    GRAV_CONST = 6.674 * 10 ** (-11)

    def __init__(self, mass: int, position: list, velocity: list):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def get_coordinates(self):
        """Returns x and y coordinates of an object.

        Returns
        -------
            Position: list[int]
        """

        return self.position

    def get_velocity(self):
        """Returns x and y components of velocity.

        Returns
        -------
            Velocity: list[int]
        """

        v_x, v_y = self.velocity
        return np.sqrt(v_x ** 2 + v_y ** 2)

    def calc_distance(self, position):
        """Calculates the distance between self and position.

        Parameters
        ----------
        position : list[int]
            list that stores objects x and y coordinates in m.

        Returns
        -------
        distance : list[int]
            Distance from self to position. Contains x and y components and real value in that order.
        """
        distance = [position[0] - self.position[0], position[1] - self.position[1]]
        distance.append(np.sqrt(distance[0] ** 2 + distance[1] ** 2))
        return distance

    def calc_force(self, celestial):
        """Calculates the gravitational force between self and celestial.

        Parameters
        ----------
        celestial : CelestialObject

        Returns
        -------
        force : list[int]
            Gravitational force exerted by celestial. Contains x and y components and real value in that order.    
        """
        # Distance = [distance_x, distance_y, distance]
        distance = self.calc_distance(celestial.position)
        force = [SpaceObject.GRAV_CONST * self.mass * celestial.mass / (distance[2] ** 2)]
        force.insert(0, force[-1] * distance[1] / distance[2])
        force.insert(0, force[-1] * distance[0] / distance[2])
        return force

    def calc_acceleration(self, celestials):
        """Calculates acceleration by summing gravitational force from all celestials on self.

        Parameters
        ----------
        celestials : Dict
            Dict that stores all celestial objects.

        Returns
        -------
        acceleration : list[int]
            Acceleration calculated with resultant of gravitational forces from all celestials.
            Contains x and y components.
        """

        sum_force = [0, 0]
        for celestial in celestials.items():
            if self is not celestial[1]:
                force = self.calc_force(celestial[1])
                sum_force[0] += force[0]
                sum_force[1] += force[1]
        acceleration = [sum_force[0] / self.mass, sum_force[1] / self.mass]
        return acceleration

    def update_attributes(self, celestials, timestamp):
        """Calculates acceleration and updates attributes.

        Parameters
        ----------
        celestials : Dict
            Dict that stores all celestial objects.
        timpestamp : int
            Simulation timestamp value.            
        """

        acceleration = self.calc_acceleration(celestials)

        # Calculating x and y components of velocity
        self.velocity[0] = self.velocity[0] + acceleration[0] * timestamp
        self.velocity[1] = self.velocity[1] + acceleration[1] * timestamp

        # Calculating new x and y coordinates
        self.position[0] = self.position[0] + self.velocity[0] * timestamp
        self.position[1] = self.position[1] + self.velocity[1] * timestamp


class Spacecraft(SpaceObject):
    """
    A class used to represent a spacecraft. It inherits the functionality from SpaceObject class. 

    Attributes:
    ----------
    fuel : int
        Amount of fuel.
    """

    def __init__(self, mass: int, position: list, velocity: list, fuel: int):
        super().__init__(mass, position, velocity)
        self.fuel = fuel


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


sim = SolarSystemSimulation()

sim.animation()
