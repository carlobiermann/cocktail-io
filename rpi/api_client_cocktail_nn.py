# Paying around with socket programm based on the code from PyMOTW found here: https://pymotw.com/3/socket/tcp.html
import socket
import sys
import time
import struct
import random

class nnclient:

    #init
    def __init__(self, serverip, port):
            self.serverip = serverip
            self.port = port      

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

        return self.message

        ##############################################
        # testing for right params @ values emotions/temp/alc
        # if not in coorect input format raise exception
        ###############################################

        if (max(self.values_emotions) > 6) or (min(self.values_emotions) < 0):
            raise Exception("false params at emotions values.")
        if (self.value_temp > 125) or (self.value_temp < -55):
            raise Exception("false params at temperature.")
        if (self.value_alc > 125) or (self.value_alc < -55):
            raise Exception("false params at alcohol-meter.")

    #send data to server and get answer
    def senddata(self, message, mode, buffersize):
        ###############################
        # mode have to be = "query", "training"
        # message have to be = single int for training, list int for query
        #
        # return, mode query = list of six elements in form of 
        # [x1(cocktail number),x2,x3,y1(percent of cocktail),y2,y3]
        #
        # return, mode trainign = "true"
        #
        ###############################

        self.message = message

        try:
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            self.server_address = (self.serverip, self.port)
                
            print('connecting to {} port {}'.format(*self.server_address))
            self.sock.connect(self.server_address)

        except ConnectionRefusedError:
            raise Exception("can't reach server.")

        if mode == "query":

            #convert to byte array
            self.message = bytearray(self.message)
            
            try:

                # Send data
                print('sending {!r}'.format(self.message))
                self.sock.sendall(self.message)
                
                #variable for exit while loop
                self.waitforreceive = 1

                while self.waitforreceive == 1:
                    self.data = self.sock.recv(buffersize)

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
                print('received nn data')
                self.sock.close()

        elif mode == "training":
            #check if choosen cocktail is in range of answer from nn, if not, exception
            if ((self.message in self.data) == False):
                raise Exception("cant progress these trainingsdata - user cant choose these cocktail")
            else:
                #convert to byte array
                self.choosencocktail_list = [0 , 0]

                self.choosencocktail_list[0] = 1
                self.choosencocktail_list[1] = int(self.message)
                self.message_training = bytearray(self.choosencocktail_list)

                try:

                    # Send data
                    print('sending {!r}'.format(self.message_training))
                    self.sock.sendall(self.message_training)

                    #variable for exit while loop
                    self.waitforreceive = 1

                    while self.waitforreceive == 1:
                        self.training_data = self.sock.recv(buffersize)

                        #return answer from server
                        print("received...")
                        print(self.training_data)
                        return True

                        #intern exit for while lop
                        if not(self.training_data) == 0:
                            self.waitforreceive = 0
                        else:
                            pass
                    
                    self.waitforreceive = 1
            
                finally:
                    print('closing socket')
                    self.sock.close()   
 

#client = nnclient("localhost", 10000)
#ran_floats = [random.randrange(6) for _ in range(100)]
#temp_temperature = random.randrange(20)+10
#print("temp", temp_temperature)
#temp_alc = random.randrange(75)
#print("alc", temp_alc)
#array_values_emotions = ran_floats#[0,1,2,3,4,5,6,0,1,4,3,4,5,7,0,6,5,4,3,2,1,0,2,1,3,4,5,3,2,4,1,3,3,5,2,1,2,4]
#data_query = client.formatdata(temp_temperature, temp_alc, array_values_emotions)
#nnvalues = client.senddata(data_query,"query", 1024)
#time.sleep(2)
#client.senddata(nnvalues[random.randrange(3)],"training", 1024)
