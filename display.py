import os
import tkinter as tk
from display.fluidapp import FluidManagementApp
from pi.pump import Pump
from pi.scale import Scale

os.environ['DISPLAY'] = ':0'

if __name__ == "__main__":
    root = tk.Tk()
    app = FluidManagementApp(root)
    app.add_container(Scale(5,6), Pump(1,2))
    app.add_container(Scale(5,6), Pump(1,2))
    root.mainloop()
