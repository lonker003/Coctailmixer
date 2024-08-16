
from scale import scale
import time
import RPi.GPIO as GPIO
scale1 = scale(5,6,1,1)
try:
    scale1.init_offset()
    while True:
        value = scale1.read_hx711()
        if value is not None:
            print(f"HX711 Reading: {value} in gr")
        else:
            print("Failed to read from HX711")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Cleaning up...")
    GPIO.cleanup()

except Exception as e:
    print(f"An error occurred: {e}")
    GPIO.cleanup()