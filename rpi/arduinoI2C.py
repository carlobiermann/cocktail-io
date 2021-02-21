import smbus
import time

bus = smbus.SMBus(1)

# slave address
address = 0x05

def readSensors():
    # empty data array
    data = bus.read_i2c_block_data(address, 99, 5);
    return data

def sendData(data):
    bus.write_byte(address, data)
