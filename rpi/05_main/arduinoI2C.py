import smbus
import time

bus = smbus.SMBus(1)

# slave address
address = 0x05

def readSensors():
    # empty data array
    data = []

    # run loop for 10 seconds
    timeout = time.time() + 10

    while time.time() < timeout:
        for i in range(0, 3):
                #data.append(bus.read_byte(address))
                val = bus.read_byte(address)
                data.insert(i, val)
        time.sleep(1)

    return data

def sendDrink(drinkChoice):
    bus.write_byte(address, drinkChoice)
