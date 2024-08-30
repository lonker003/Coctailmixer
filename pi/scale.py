import RPi.GPIO as GPIO
import time

class Scale:
    dt: int
    sck: int
    offset: float
    reference_unit:float

    def __init__(self, dt, sck):
        self.dt = dt
        self.sck = sck

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dt, GPIO.IN)
        GPIO.setup(sck, GPIO.OUT)
        
    def init_offset(self):
        self.offset = self.calculate_offset()
        self.referenz_unit = -19000/247

    def read(self) -> float:
        value = self.read_hx711()
        return (value-self.offset)/self.referenz_unit

    def read_hx711(self) -> int:
        count = 0
        for _ in range(24):
            GPIO.output(self.sck, 1)
            count = count << 1
            GPIO.output(self.sck, 0)
            if GPIO.input(self.dt):
                count += 1
        
        GPIO.output(self.sck, 1)
        GPIO.output(self.sck, 0)

        if count & 0x800000:
            count = -(count ^ 0xFFFFFF) - 1

        return count
        

    def calculate_offset(self) -> float:
        sum : int  = 0
        for _ in range(20):
            sum += self.read_hx711()
            time.sleep(0.1)
            
        return sum/20
