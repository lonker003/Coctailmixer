import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont 
from ..pi.pump import Pump
from ..pi.scale import Scale

class FluidContainer(ttk.Frame):
    pump: Pump
    scale: Scale

    def __init__(self, master, scale: Scale,pump: Pump):
        super().__init__(master, padding="10")
        self.name_var = tk.StringVar(value=f"Container")
        self.pump = pump
        self.scale = scale

        self.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)

        self.name_entry = ttk.Entry(self, textvariable=self.name_var, font=('Helvetica', 24))
        self.name_entry.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        
        self.weight_var = tk.StringVar(value=f"")
        self.update()
        ttk.Label(self, textvariable=self.weight_var, font=('Helvetica', 24)).grid(row=2, rowspan=2, column=0, sticky="n")

        helv24 = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        self.pump_button = tk.Button(self, text="Pump", font= helv24)        
        self.pump_button.grid(row=4, rowspan=4, column=0, sticky="nsew", pady=(20, 20))
        self.pump_button.bind("<ButtonPress-1>", self.start_pump)
        self.pump_button.bind("<ButtonRelease-1>", self.stop_pump)

        tk.Button(self, text="Keyboard", command=self.show_keyboard).grid(row=8,column=0)

    def update(self):
        self.weight_var.set(f"Weight: {self.scale.read}%")

    def start_pump(self, event):
        self.pump.toggle()

    def stop_pump(self, event):
        self.pump.toggle()
        
    def show_keyboard(self):
        subprocess.Popen(["onboard"])
