import time
import smbus

class Heat:
  def __init__(self):
    self.address = 0x38
    self.i2cbus = smbus.SMBus(1)
    time.sleep(0.5)

    data = self.i2cbus.read_i2c_block_data(self.address,0x71,1)
    if (data[0] | 0x08) == 0:
      print('Initialization error')
  
  
  def read(self) -> float:
    self.i2cbus.write_i2c_block_data(self.address,0xac,[0x33,0x00])
    time.sleep(0.1)

    data = self.i2cbus.read_i2c_block_data(self.address,0x71,7)

    Traw = ((data[3] & 0xf) << 16) + (data[4] << 8) + data[5]
    temperature = 200*float(Traw)/2**20 - 50

    Hraw = ((data[3] & 0xf0) >> 4) + (data[1] << 12) + (data[2] << 4)
    humidity = 100*float(Hraw)/2**20

    return temperature
