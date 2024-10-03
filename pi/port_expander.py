import time
import smbus2

# MCP23017 Register Definitions
IODIRA = 0x00  # I/O direction register for port A
IODIRB = 0x01  # I/O direction register for port B
GPIOA = 0x12   # Register for reading Port A
GPIOB = 0x13   # Register for reading Port B
OLATA = 0x14   # Register for writing Port A
OLATB = 0x15   # Register for writing Port B

class MCP23017:
    def __init__(self, address=0x20, bus_num=1):
        self.bus = smbus2.SMBus(bus_num)
        self.address = address
        # Set both A and B ports to input by default (1 = input, 0 = output)
        self.bus.write_byte_data(self.address, IODIRA, 0xFF)
        self.bus.write_byte_data(self.address, IODIRB, 0xFF)

    def set_pin_mode(self, pin, mode):
        if pin < 8:
            reg = IODIRA
        else:
            reg = IODIRB
            pin -= 8

        current_mode = self.bus.read_byte_data(self.address, reg)
        if mode == 'output':
            current_mode &= ~(1 << pin)
        elif mode == 'input':
            current_mode |= (1 << pin)

        self.bus.write_byte_data(self.address, reg, current_mode)

    def digital_write(self, pin, value):
        if pin < 8:
            reg = OLATA
        else:
            reg = OLATB
            pin -= 8

        current_value = self.bus.read_byte_data(self.address, reg)
        if value == 1:
            current_value |= (1 << pin)
        else:
            current_value &= ~(1 << pin)

        self.bus.write_byte_data(self.address, reg, current_value)

    def digital_read(self, pin):
        if pin < 8:
            reg = GPIOA
        else:
            reg = GPIOB
            pin -= 8

        value = self.bus.read_byte_data(self.address, reg)
        return (value >> pin) & 1

class HX711:
    def __init__(self, mcp, dt, sck):
        self.mcp = mcp
        self.dt = dt
        self.sck = sck

        # Set pin modes
        self.mcp.set_pin_mode(dt, 'input')
        self.mcp.set_pin_mode(sck, 'output')
        
        # Set SCK to low
        self.mcp.digital_write(self.sck, 0)

    def read(self):
        # Wait for the chip to become ready
        print("Waiting for HX711 to become ready...")
        ready_counter = 0
        while self.mcp.digital_read(self.dt) == 1:
            ready_counter += 1
            if ready_counter > 1000:  # Timeout after 1000 attempts
                print("Timeout waiting for HX711 to become ready")
                return None
        print(f"HX711 ready after {ready_counter} checks")

        # Read 24 bits
        data = 0
        for i in range(24):
            self.mcp.digital_write(self.sck, 1)
            time.sleep(0.000001)  # 1 microsecond delay
            self.mcp.digital_write(self.sck, 0)
            time.sleep(0.000001)  # 1 microsecond delay
            bit = self.mcp.digital_read(self.dt)
            data = (data << 1) | bit
            print(f"Bit {i}: {bit}")

        # 25th pulse to finish the conversation
        self.mcp.digital_write(self.sck, 1)
        time.sleep(0.000001)  # 1 microsecond delay
        self.mcp.digital_write(self.sck, 0)
        time.sleep(0.000001)  # 1 microsecond delay

        # Convert to signed value
        if data & 0x800000:
            data -= 1 << 24

        print(f"Raw data: {data}")
        return data

    def power_down(self):
        self.mcp.digital_write(self.sck, 0)
        self.mcp.digital_write(self.sck, 1)
        time.sleep(0.00006)

    def power_up(self):
        self.mcp.digital_write(self.sck, 0)

# Example usage
mcp = MCP23017(address=0x27, bus_num=1)
hx711 = HX711(mcp, dt=3, sck=2)

print("Starting continuous read. Press CTRL+C to stop.")
try:
    while True:
        hx711.power_up()
        value = hx711.read()
        hx711.power_down()
        if value is not None:
            print(f"HX711 reading: {value}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped.")
finally:
    hx711.power_down()