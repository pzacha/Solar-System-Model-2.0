import tkinter as tk

from solar_system_model.simulation import SolarSystemSimulation


class UserInterface:
    """
    A user interface class.
    """

    def __init__(self):
        # Create window and set its properties.
        self.window = tk.Tk()
        self.window.title("Solar system model")
        self.window.geometry("350x200")

        # Create buttons.
        self.start = tk.Button(self.window, text="Simulation", command=self.start_simulation)
        self.start.grid(column=0, row=6)

        # Define inputs
        self.timestep_desc = tk.Label(self.window, text="Timestep value: ")
        self.timestep_desc.grid(column=0, row=0)
        self.timestep = tk.Entry(self.window, width=8)
        self.timestep.grid(column=1, row=0)
        self.timestep_unit = tk.Label(self.window, text="seconds.")
        self.timestep_unit.grid(column=2, row=0)

        # Define checkbuttons
        self.check_planets = tk.Label(self.window, text="Choose planets for simulation.")
        self.check_planets.grid(column=1, row=0)
        self.mercury_state = tk.BooleanVar(value=True)
        self.mercury_btn = tk.Checkbutton(self.window, text="Mercury", variable=self.mercury_state, width=8)
        self.mercury_btn.grid(row=2, column=0)
        self.venus_state = tk.BooleanVar(value=True)
        self.venus_btn = tk.Checkbutton(self.window, text="Venus", variable=self.venus_state, width=8)
        self.venus_btn.grid(row=3, column=0)
        self.earth_state = tk.BooleanVar(value=True)
        self.earth_btn = tk.Checkbutton(self.window, text="Earth", variable=self.earth_state, width=8)
        self.earth_btn.grid(row=4, column=0)
        self.mars_state = tk.BooleanVar(value=True)
        self.mars_btn = tk.Checkbutton(self.window, text="Mars", variable=self.mars_state, width=8)
        self.mars_btn.grid(row=5, column=0)
        self.jupiter_state = tk.BooleanVar(value=True)
        self.jupiter_btn = tk.Checkbutton(self.window, text="Jupiter", variable=self.jupiter_state, width=8)
        self.jupiter_btn.grid(row=2, column=1)
        self.saturn_state = tk.BooleanVar(value=True)
        self.saturn_btn = tk.Checkbutton(self.window, text="Saturn", variable=self.saturn_state, width=8)
        self.saturn_btn.grid(row=3, column=1)
        self.neptune_state = tk.BooleanVar(value=True)
        self.neptune_btn = tk.Checkbutton(self.window, text="Neptune", variable=self.neptune_state, width=8)
        self.neptune_btn.grid(row=4, column=1)
        self.uranus_state = tk.BooleanVar(value=True)
        self.uranus_btn = tk.Checkbutton(self.window, text="Uranus", variable=self.uranus_state, width=8)
        self.uranus_btn.grid(row=5, column=1)

        # Start GUI.
        self.window.mainloop()

    def set_timestep(self, s):
        """Checks if timestep is correct. If not, set the value to default.
        """
        try:
            int(s)
        except:
            self.timestep.delete(0, "end")
            self.timestep.insert(0, 3600)

    def get_checkbuttons_values(self):
        """Gets checkbuttons values and prepares dictionary with planets chosen for simulation.

        Returns
        -------
        planets : dict
            Dictionary with planets chosen for simulation.
        """

        planets = {}
        planets["Mercury"] = self.mercury_state.get()
        planets["Venus"] = self.venus_state.get()
        planets["Earth"] = self.earth_state.get()
        planets["Mars"] = self.mars_state.get()
        planets["Jupiter"] = self.jupiter_state.get()
        planets["Saturn"] = self.saturn_state.get()
        planets["Uranus"] = self.uranus_state.get()
        planets["Neptune"] = self.neptune_state.get()

        return planets

    def start_simulation(self):
        """
        Method that starts the simulation. Used for start button. 
        It checks if Entry value is correct.
        """

        # Get timestep value
        self.set_timestep(self.timestep.get())

        # Create simulation instance
        sim = SolarSystemSimulation(int(self.timestep.get()))

        # Load chosen planets
        planets = self.get_checkbuttons_values()
        sim.insert_celestials(planets)

        # Start simulation
        sim.animation()
