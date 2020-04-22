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
        self.start.grid(column=1, row=1)

        # Define inputs
        self.timestep_desc = tk.Label(self.window, text="Timestep value: ")
        self.timestep_desc.grid(column=0, row=0)
        self.timestep = tk.Entry(self.window, width=8)
        self.timestep.grid(column=1, row=0)
        self.timestep_unit = tk.Label(self.window, text="seconds.")
        self.timestep_unit.grid(column=2, row=0)

        # Start GUI.
        self.window.mainloop()

    def set_timestep(self, s):
        try:
            int(s)
        except:
            self.timestep.delete(0, "end")
            self.timestep.insert(0, 3600)

    def start_simulation(self):
        """
        Method that starts the simulation. Used for start button. 
        It checks if Entry value is correct.
        """

        self.set_timestep(self.timestep.get())
        sim = SolarSystemSimulation(int(self.timestep.get()))
        sim.animation()
