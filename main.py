
from scale import scale
from heat import heat
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import os
scale1 = scale(5,6,1,1)
heat1 = heat()
try:
    
    scale1.init_offset()
    data_list = [[],[],[]]
    time_= 0
    
    if os.path.exists("output.txt"):
        os.remove('output.txt')
    with open('output.txt', 'a') as file:
        file.write('Temperatur\tGewicht\tZeit\n')
        while True:
            temperatur = heat1.read()
            value = scale1.read_hx711()
            if value is not None:
                file.write(f"{round(temperatur,4)}\t{round(value,4)}\t{round(time_,2)}\n")
                print(f"HX711 Reading: {value} in gr , Temperatur: {temperatur} in Grad")
            else:
                print("Failed to read from HX711")
            time.sleep(0.2)
            time_=time_+0.2
        
    

except KeyboardInterrupt:
    print("Cleaning up...")
    GPIO.cleanup()

except Exception as e:
    print(f"An error occurred: {e}")
    GPIO.cleanup()