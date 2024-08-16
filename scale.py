import RPi.GPIO as GPIO
import time
import numpy as np

class scale:
    def __init__(self, dt, sck,offset,referenz_unit):
        self.dt = dt
        self.sck = sck
        self.offset = offset
        self.referenz_unit = referenz_unit
        
        # GX711 pin configuration
        #DT_PIN = 5
        #SCK_PIN = 6

        # Initialize the GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dt, GPIO.IN)
        GPIO.setup(sck, GPIO.OUT)
        
    def init_offset(self):
        print("Starting HX711 reading loop")
        self.offset = self.calculate_offset()
        self.referenz_unit = -19000/247
        print(self.offset)

    def read_hx711(self):
        # Read 24 bits of data
        count = 0
        for i in range(24):
            GPIO.output(self.sck, 1)
            count = count << 1
            GPIO.output(self.sck, 0)
            if GPIO.input(self.dt):
                count += 1
        
        GPIO.output(self.sck, 1)
        GPIO.output(self.sck, 0)

        # Convert 2's complement to integer
        if count & 0x800000:
            count = -(count ^ 0xFFFFFF) - 1
        
        return (count-self.offset)/self.referenz_unit

    def calculate_offset(self):
        i = 0
        current_readings = []
        while(i<=20):
            current_readings.append(self.read_hx711())
            time.sleep(0.1)
            i= i+1
            
        return np.median(current_readings)

    