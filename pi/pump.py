class Pump:
    on: bool = False
    pin1: int
    pin2: int

    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2

    def toggle(self):
        self.on = not self.on
