import smbus
import time

bus = smbus.SMBus(1)

# slave address
address = 0x05

def readSensors():
    # empty data array
    data = bus.read_i2c_block_data(address, 99, 3);
    return data

def sendDrink(drinkChoice):
    bus.write_byte(address, drinkChoice)
