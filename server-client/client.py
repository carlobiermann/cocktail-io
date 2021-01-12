# Paying around with socket programm based on the code from PyMOTW found here: https://pymotw.com/3/socket/tcp.html
import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'Message to all clients'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    while True:
        data = sock.recv(8)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
