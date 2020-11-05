import smbus
import time

bus = smbus.SMBus(1)
addr = 0x05
lastState = 0

def readData():
    data = bus.read_byte(addr)
    return data

while True:
    rxData = readData()
    if rxData != lastState :
        print("The button was pressed")
    lastState = rxData
