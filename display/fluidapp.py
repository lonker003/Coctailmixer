import tkinter as tk
from tkinter import ttk
import sv_ttk
from fluidcontainer import FluidContainer
from ..pi.pump import Pump
from ..pi.scale import Scale

class FluidManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Fluid Management System")

        sv_ttk.set_theme("dark")
        #master.attributes('-fullscreen', True)
        master.bind('<Escape>', self.end_fullscreen)

        self.main_frame = ttk.Frame(master, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.container_count = 0
        self.main_frame.columnconfigure(tuple(range(2)), weight=1)
        self.main_frame.rowconfigure(tuple(range(1)), weight=1)

    def add_container(self, scale: Scale,pump: Pump):
        self.container_count+=1
        FluidContainer(self.main_frame, scale, pump).grid(row=0, column=self.container_count, sticky="nsew", padx=5, pady=5)
        self.main_frame.columnconfigure(tuple(range(self.container_count)), weight=1)

    def end_fullscreen(self, event=None):
        self.master.attributes("-fullscreen", False)
