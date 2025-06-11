import subprocess
import time

# Define the GPIO pin number you are controlling
pin_number = 4

# Function to set the GPIO pin as output
def set_pin_mode():
    subprocess.run(['pinctrl', 'set', str(pin_number), 'op'])

# Function to turn the relay ON
def turn_relay_on():
    subprocess.run(['pinctrl', 'set', str(pin_number), 'dl'])

# Function to turn the relay OFF
def turn_relay_off():
    subprocess.run(['pinctrl', 'set', str(pin_number), 'dh'])

# Main function to control the relay
def control_relay():
    set_pin_mode()  # Set the pin as output
    try:
        while True:
            print("Relay ON")
            turn_relay_on()  # Turn the relay ON
            time.sleep(2)  # Leave it on for 5 seconds
            
            print("Relay OFF")
            turn_relay_off()  # Turn the relay OFF
            time.sleep(2)  # Leave it off for 5 seconds
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        turn_relay_off()  # Ensure the relay is turned OFF on exit

# Run the control relay function
if __name__ == "__main__":
    control_relay()
