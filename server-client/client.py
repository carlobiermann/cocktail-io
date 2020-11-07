# Paying around with socket programm based on the code from PyMOTW found here: https://pymotw.com/3/socket/tcp.html
import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
time.sleep(1)
print('connecting to {} port {}'.format(*server_address))
time.sleep(1)
sock.connect(server_address)
time.sleep(1)

try:

    # Send data
    message = b'This is the message.  It will be repeated.'
    time.sleep(1)
    print('sending {!r}'.format(message))
    time.sleep(1)
    sock.sendall(message)
    time.sleep(1)

    # Look for the response
    amount_received = 0
    time.sleep(1)
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1)
        amount_received += len(data)
        time.sleep(1)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    time.sleep(1)
    sock.close()
