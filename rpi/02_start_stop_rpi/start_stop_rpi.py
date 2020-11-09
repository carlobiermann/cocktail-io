import smbus
import time
import printerFunc

bus = smbus.SMBus(1)
addr = 0x05

def readData():
    data = bus.read_byte(addr)
    return data

lastState = readData()

while True:
    rxData = readData()
    while rxData != lastState :
        printerFunc.printer()
        if rxData != lastState:
            break
    lastState = readData()
