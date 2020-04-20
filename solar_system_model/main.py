# from models import SpaceObject, Spacecraft
# from simulation import SolarSystemSimulation
from solar_system_model.models import SpaceObject, Spacecraft
from solar_system_model.simulation import SolarSystemSimulation

sim = SolarSystemSimulation(3600)

sim.animation()
