import smbus
import time
bus = smbus.SMBus(1)

address = 0x05

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    send = input("Integer between 1 - 9: ")
    if not send:
        continue

    writeNumber(send)
    print ("RPI sending this integer: ", send)
    time.sleep(1)

    receive = readNumber()
    print("Arduino receives this integer: ", receive)
