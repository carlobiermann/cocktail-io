# Paying around with socket programm based on the code from PyMOTW found here: https://pymotw.com/3/socket/tcp.html
import socket
import sys
import time
import struct


class nnclient:

    #init
    def __init__(self, serverip, port):
        try:
            self.serverip = serverip
            self.port = port
        
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            self.server_address = (self.serverip, self.port)
            print('connecting to {} port {}'.format(*self.server_address))
            self.sock.connect(self.server_address)

        except ConnectionRefusedError:
            raise Exception("can't reach server.")
            pass

    #format the data for sending to nn 
    def formatdata(self, val_alc, val_temp, values_emotions):

        #TO-DO Verify val_alc format

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

        ##############################################
        # testing for right params @ values emotions/temp/alc
        # if not in coorect input format raise exception
        ###############################################

        if (max(self.values_emotions) > 6) or (min(self.values_emotions) < 0):
            raise Exception("false params at emotions values.")
        if (max(self.val_temp) > 125) or (min(self.val_temp) < -55):
            raise Exception("false params at temperature.")
        if (max(self.val_alc) > 125) or (min(self.val_alc) < -55):
            raise Exception("false params at alcohol-meter.")

    #send data to server and get answer
    def senddata(self):

        #convert to byte array
        self.message = bytearray(self.message)
        
        try:

            # Send data
            print('sending {!r}'.format(self.message))
            self.sock.sendall(self.message)
            
            #variable for exit while loop
            self.waitforreceive = 1

            while self.waitforreceive == 1:
                self.data = self.sock.recv(4096)

                #converting to float
                self.data = struct.unpack('<6f', self.data)
                
                #return answer from server
                print("received...")
                print(list(self.data))
                return self.data

                #intern exit for while lop
                if not(self.data) == 0:
                    self.waitforreceive = 0
                else:
                    pass
            
            self.waitforreceive = 1
       
        finally:
            print('closing socket')
            self.sock.close()
        
    


client = nnclient("localhost", 10000)
array_values_emotions = [0,1,2,3,4,5,6,0,1,2,3,4,5,6,0,6,5,4,3,2,1,0,2,1,3,4,5,3,2,4,1,3,3,5,2,1,2,4]
client.formatdata(50, 75, array_values_emotions)
client.senddata()