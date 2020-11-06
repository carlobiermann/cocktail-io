import time 
import smbus

bus = smbus.SMBus(1)
addr = 0x05

def readData():
    data = bus.read_byte(addr)
    return data

lastState = readData()

def printer():
    lastState = readData()

    while True:
        rxData = readData()
        print("Running the function...")
        time.sleep(1)

        if rxData != lastState :
            break


