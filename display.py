import os
import subprocess
import tkinter as tk
from tkinter import ttk
import sv_ttk

from tkinter import font as tkFont 


# Set the DISPLAY variable to use the Pi's physical display
os.environ['DISPLAY'] = ':0'


class FluidContainer(ttk.Frame):
    def __init__(self, master, name):
        super().__init__(master, padding="10")
        self.name_var = tk.StringVar(value=f"Container {name}")
        self.weight = 0

        self.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=1)

        # Editable name field
        self.name_entry = ttk.Entry(self, textvariable=self.name_var, font=('Helvetica', 24))
        self.name_entry.grid(row=0, column=0, sticky="ew", pady=(0, 5))
        
        self.weight_var = tk.StringVar(value=f"Füllstand: {self.weight} %")
        ttk.Label(self, textvariable=self.weight_var, font=('Helvetica', 24)).grid(row=2, rowspan=2, column=0, sticky="n")

        helv24 = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
        self.pump_button = tk.Button(self, text="Pump", font= helv24, command=self.pump)        
        self.pump_button.grid(row=4, rowspan=4, column=0, sticky="nsew", pady=(20, 20))

        self.pump_button.bind("<ButtonPress-1>", self.start_pump)
        self.pump_button.bind("<ButtonRelease-1>", self.stop_pump)
        tk.Button(self, text="Keyboard", command=self.show_keyboard).grid(row=8,column=0)

    def pump(self):
        self.weight += 10  # Increase weight by 10g each pump
        self.weight_var.set(f"Füllstand: {self.weight}%")

    def start_pump(self, event):
        print("pressed")

    def stop_pump(self, event):
        print("stop")
        
    def show_keyboard(self):
        subprocess.Popen(["onboard"])

class FluidManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Fluid Management System")

        # Apply the Sun Valley theme
        sv_ttk.set_theme("dark")

        # Make the window fullscreen
        master.attributes('-fullscreen', True)

        # Bind Escape key to exit fullscreen
        master.bind('<Escape>', self.end_fullscreen)

        # Create a main frame
        self.main_frame = ttk.Frame(master, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Configure grid
        self.main_frame.columnconfigure(tuple(range(2)), weight=1)
        self.main_frame.rowconfigure(tuple(range(1)), weight=1)



        self.containers = []
        self.next_position = (1, 0)  # Start adding containers from the second row
        self.add_container()
        self.add_container()

    def add_container(self):
        if len(self.containers) < 8:  # Limit to 8 containers (2 rows of 4)
            container = FluidContainer(self.main_frame, len(self.containers) + 1)
            row, col = self.next_position
            container.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
            self.containers.append(container)

            # Update next position
            col += 1
            if col > 3:
                col = 0
                row += 1
            self.next_position = (row, col)
        else:
            print("Maximum number of containers reached.")
    

    def end_fullscreen(self, event=None):
        self.master.attributes("-fullscreen", False)

if __name__ == "__main__":
    root = tk.Tk()
    app = FluidManagementApp(root)
    root.mainloop()
    app.add_container()
    app.add_container()