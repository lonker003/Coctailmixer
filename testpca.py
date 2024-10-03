
import smbus

PCA9548_ADDR = 0x70
bus = smbus.SMBus(1)

def select_channel(channel):
    # Aktiviert den gewünschten Kanal
    bus.write_byte(PCA9548_ADDR, 1 << channel)

# Beispiel: Kanal 0 auswählen
select_channel(0)