# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

## Define the NN ##
input_nodes = 15
hidden_nodes = 10
output_nodes = 10
learning_rate  = 0.3
training_epoch = 1

debug_mode = 0

path_to_trainingsdata = "mnist_dataset\mnist_train_100.csv"
path_to_debugdata = "mnist_dataset\mnist_test_10.csv"

serverip = "localhost"
port = 10000

##########################################################

import body_cocktail_nn as nn
import numpy as np 
import os
import datetime
import socket
import sys
import time

##########################################################
class cocktailapp:
    
    #init
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate, path_to_trainingsdata, training_epoch, path_to_debugdata, debug_mode):
         
        self.script_dir = os.path.dirname(__file__)
        self.int_data_path = os.path.join(self.script_dir, path_to_trainingsdata)
        self.path_to_debugdata = os.path.join(self.script_dir, path_to_debugdata)
        self.path_to_wih = os.path.join(self.script_dir, "saved_wih.npy")
        self.path_to_who = os.path.join(self.script_dir, "saved_who.npy")
        
        #installing new nn   
        self.n = nn.neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate, self.path_to_wih, self.path_to_who)

        #variables 
        self.oonodes = output_nodes
        self.training_epoch = training_epoch
        self.debug_mode = debug_mode

        #says done, debugging
        print("Put up Neuronal Net Body...") 

    #train new nn with data
    def firsttrain(self):
        
        #check if weights already exists
        try:
            f = open(self.path_to_wih, "r")
            f.close()
            f = open(self.path_to_who, "r")
            f.close()

        except FileNotFoundError:
            print("No trained net found. Training new one!")
            #load the nn training data
            self.training_data_file = open(self.int_data_path, "r")
            self.training_data_list = self.training_data_file.readlines()
            self.training_data_file.close()
            print(len(self.training_data_list),"records in training files")

            #how often trainingdata were used
            for e in range(self.training_epoch):
                #loop for every record
                for record in self.training_data_list:
                    print("in loop!")
                    #format record
                    self.all_values = record.split(',')
                    #scale and shift the inputs
                    self.inputs = (np.asfarray(self.all_values[1:]) / 255.0 * 0.99) + 0.01
                    #create the target output values (all 0.01, expect the desired label which is 0.99)
                    self.targets = np.zeros(self.oonodes) + 0.01
                    #all_values[0] ist target label for this record
                    self.targets[int(self.all_values[0])] = 0.99
                    self.n.train(self.inputs, self.targets)
            pass

        else:
            #saved wih and who files are found
            print("Trained net found and used.")
            self.n.loadweights()

        #says done
        print("Neuronal net ready.")
        pass

    #get actual date and time 
    def getdate(self):
        #get date and time for additional data point
        self.datetime = datetime.datetime.now()

        #instance for list
        self.time_list_unconverted = [0, 1, 2, 3, 4, 5]
        self.time_list = [0, 1, 2, 3, 4, 5]

        #format: 
        self.time_list_unconverted[0] = int(self.datetime.strftime("%m")) #month
        self.time_list_unconverted[1] = int(self.datetime.strftime("%d")) #day
        self.time_list_unconverted[2] = int(self.datetime.strftime("%H")) #hour 24-format
        self.time_list_unconverted[3] = int(self.datetime.strftime("%M")) #minute
        self.time_list_unconverted[4] = int(self.datetime.strftime("%S")) #second 
        self.time_list_unconverted[5] = int(datetime.datetime.today().weekday()) #weekday, 0 monday - 6 sunday

        #scale time values from 0.01 to 1
        self.time_list[0] = (self.time_list_unconverted[0] / 12 * 0.99) + 0.01 #12 months
        self.time_list[1] = (self.time_list_unconverted[1] / 31 * 0.99) + 0.01 #31 days
        self.time_list[2] = (self.time_list_unconverted[2] / 23 * 0.99) + 0.01 #23 hours
        self.time_list[3] = (self.time_list_unconverted[3] / 59 * 0.99) + 0.01 #59 mins
        self.time_list[4] = (self.time_list_unconverted[4] / 59 * 0.99) + 0.01 #59 secods 
        self.time_list[5] = (self.time_list_unconverted[5] / 6 * 0.99) + 0.01 #6 + 1 days -> 0!

        return self.time_list

    #train neuronal net from input
    def retrain(self):
        
        #check for debug mode
        if self.debug_mode == 0:
            #TO-DO: train funktion activ net
            #...
            self.n.saveweights()
            pass
        else:
            pass
    
    #query for the right cocktail
    def query(self, input_list):
        
        #query the nn 
        self.input_list=input_list
        self.outputs_list = self.n.query(input_list)

        #fallback "error"-handling if nn produces probabilities over 100%
        # for x in self.outputs_list:
        #     if self.outputs_list[x] > 1:
        #         print("Oops! Something went wrong. Setting fallback values of 10 percent for each.")
        #         for x in self.outputs_list:
        #             self.outputs_list[x] = 0.1 
        #     else:
        #         pass  
        
        return self.outputs_list
    
    #debug and testing function
    def chkdebug(self):
        self.test_data_file = open(self.path_to_debugdata, "r")
        self.test_data_list = self.test_data_file.readlines()
        self.test_data_file.close()

        self.all_values = self.test_data_list[3].split(",")
        print(self.all_values[0])
        self.all_values_transported = (np.asfarray(self.all_values[1:]) / 255.0 * 0.99) + 0.01
        self.a = self.n.query(self.all_values_transported)
        print(self.a)

        self.n.saveweights()

def startingsocket(serverip, port):
    # Create a TCP/IP socket
    global sock

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 

    # Bind the socket to the port
    server_address = (serverip, port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

def sortingdata(data, val_time):
    ################################
    # input format for data:
    # input_array[0] = 0 for syntax check
    # input_array[1] = value temperature scaled 0-255
    # input_array[2] = value alcohol scaled 0-255
    # input_array[3...] = value emotions 0-6
    ################################ 
    return_values = [1,2,3,4,5,6,7,8,9]

    temp_data = data[1]
    alc_data = data[2]
    emotions_data = data[3:]
    val_angry_0 = (emotions_data.count(0) / len(emotions_data)) + 0.01
    val_disgusted_1 = (emotions_data.count(1) / len(emotions_data)) + 0.01
    val_fearful_2 = (emotions_data.count(2) / len(emotions_data)) + 0.01
    val_happy_3 = (emotions_data.count(3) / len(emotions_data)) + 0.01
    val_neutral_4 = (emotions_data.count(4) / len(emotions_data)) + 0.01 
    val_sad_5 = (emotions_data.count(5) / len(emotions_data)) + 0.01
    val_surprised_6 = (emotions_data.count(6) / len(emotions_data)) + 0.01

    #get the rigth ordering
    return_values[0] = temp_data
    return_values[1] = alc_data
    return_values[2] = val_angry_0
    return_values[3] = val_disgusted_1
    return_values[4] = val_fearful_2
    return_values[5] = val_happy_3
    return_values[6] = val_neutral_4
    return_values[7] = val_sad_5
    return_values[8] = val_surprised_6
    return_values.extend(val_time)

    return return_values

    ###########################
    #
    # return_values : list with 15 elements
    #
    ###########################

##########################################################
app = cocktailapp(input_nodes, hidden_nodes, output_nodes, learning_rate, path_to_trainingsdata, training_epoch, path_to_debugdata, debug_mode)
startingsocket(serverip, port)
#app.firsttrain()
#app.chkdebug()

try:
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(4096)
                print(list(data))
                
                #main routine
                if data:
                    val_time = app.getdate() 
                    input_variables_to_nn = sortingdata(data,val_time) 
                    output_variables_from_nn = app.query(input_variables_to_nn)
                    print("sending answer....") 
                    print(output_variables_from_nn)  
                    #answer = ("hello!".encode("utf-8"))
                    answer = bytearray(output_variables_from_nn)
                    print(" ")
                    print(list(answer))
                    connection.sendall(answer)
                else:
                    break

        finally:
            # Clean up the connection
            connection.close()
            print("close.")

except KeyboardInterrupt:
    sock.close()
    print("Ctrl + C: terminated in front of keyboard interrupt.")
    pass