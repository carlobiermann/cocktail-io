# Paying around with socket programm based on the code from PyMOTW found here: https://pymotw.com/3/socket/tcp.html
import socket
import sys
import time


class nnclient:

    #init
    def __init__(self, serverip, port):
        #setting values
        self.serverip = serverip
        self.port = port
        
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.server_address = (self.serverip, self.port)
        print('connecting to {} port {}'.format(*self.server_address))
        self.sock.connect(self.server_address)

    #format the data for sending to nn 
    def formatdata(self, val_alc, val_temp, values_emotions):
        #############################################
        # val_temp has to: single int C° value
        # val_alc has to : single int 
        # values_emotions has to: list of ints 0 - 6
        ##############################################

        self.value_alc = val_alc
        self.value_temp = val_temp
        self.values_emotions = values_emotions
        self.message = [0,1,2,3]
        
        ##############################################
        # scaling with syntax
        # NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        ##############################################

        ##############################################
        # DS18B20 - temp - Operating: -55C° ~ 125C° ##
        ##############################################
        self.scaled_value_temp = int((((self.value_temp - (-55)) * 255) / 180) + 0) 

        ###############################################
        # FORMAT SENDING DATA 
        # a[0] = 0 (verify!)
        # a[1] = temp
        # a[2] = alcohol
        # a[3...] = data emotions z.B. 1, 1, 3, 1, 5, ....
        ###############################################
        
        self.message[0]=0
        self.message[1]=self.scaled_value_temp
        self.message[2]=self.value_alc
        self.message.extend(values_emotions)

    #send data to server and get answer
    def senddata(self):
        #convert to byte array
        self.message = bytearray(self.message)
        
        try:

            # Send data
            print('sending {!r}'.format(self.message))
            self.sock.sendall(self.message)

            self.waitforreceive = 1

            while self.waitforreceive == 1:
                self.data = self.sock.recv(4096)
                print('received {!r}'.format(self.data))
                if not(self.data) == 0:
                    self.waitforreceive = 0
                else:
                    pass
            
            self.waitforreceive = 1

        finally:
            print('closing socket')
            self.sock.close()

client = nnclient("localhost", 10000)
a = [0,3,43,23,124,0,0,0,0,0,0,0,0,0,0,0,23,23,4,4,5,3,2,1,13,4,5,3,12,4,7,23,34,5,32,1,2,34]
client.formatdata(50, 75, a)
client.senddata()