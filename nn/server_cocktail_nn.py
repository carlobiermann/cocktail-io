# Paying around with socket programm based on the code from PyMOTW found here: https://pymotw.com/3/socket/tcp.html
import socket
import sys
import time

class nnserver:

    #init
    def __init__(self, serverip, port):
        #setting values
        self.serverip = serverip
        self.port = port

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        self.server_address = (self.serverip, self.port)
        print('starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)

    #getdatainput
    def getdata(self):

        while True:
            # Wait for a connection
            print('waiting for a connection')
            self.connection, self.client_address = self.sock.accept()
            try:
                print('connection from', self.client_address)
                # Receive the data in small chunks and retransmit it
                while True:
                    self.data = self.connection.recv(4096)
                    print(self.data)
                    print(list(self.data))
                    if self.data:
                        self.answer = ("danke!").encode("utf-8")
                        self.connection.sendall(self.answer)
                    else:
                        break

            finally:
                # Clean up the connection
                self.connection.close()
                print("close.")

    def senddata(self):
        pass

server = nnserver("localhost",10000)
server.getdata()


