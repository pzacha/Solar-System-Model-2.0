import tkinter as tk

from solar_system_model.simulation import SolarSystemSimulation


class UserInterface:
    """
    A user interface class.
    """

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Solar system model")
        self.window.geometry("350x200")

        # self.lbl = tk.Label(self.window, text="Hello")
        # self.lbl.grid(column=0, row=0)

        self.btn = tk.Button(self.window, text="Simulation", command=self.start_simulation)
        self.btn.grid(column=1, row=0)

        self.window.mainloop()

    def start_simulation(self):
        sim = SolarSystemSimulation(3600)
        sim.animation()
