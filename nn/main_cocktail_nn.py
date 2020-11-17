# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

## Define the NN ##
input_nodes = 784
hidden_nodes = 100
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

class cocktailapp:
    
    #init
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate, path_to_trainingsdata, training_epoch, path_to_debugdata, debug_mode, serverip, port):
         
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
        self.serverip = serverip
        self.port = port
        self.debug_mode = debug_mode

        #says done, debugging
        print("Put up Neuronal Net Body...") 

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 

        # Bind the socket to the port
        self.server_address = (self.serverip, self.port)
        print('starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)

        # Listen for incoming connections
        self.sock.listen(1)

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
    
    #get data from cocktail-client
    def waitfordata(self):
        #TO-DO: socket loop to get data

        ################################
        # input format for data:
        # 
        ################################ 

        #self.scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        #print(scaled_input)
        #pass
        try:
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
                            print("sending answer....")   
                            self.answer = ("Hello!").encode("utf-8")
                            self.connection.sendall(self.answer)
                        else:
                            break

                finally:
                    # Clean up the connection
                    self.connection.close()
                    print("close.")

        except KeyboardInterrupt:
            self.sock.close()
            print("Press Ctrl-C to terminate while statement")
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
        for x in self.outputs_list:
            if self.outputs_list[x] > 1:
                print("Oops! Something went wrong. Setting fallback values of 10 percent for each.")
                for x in self.outputs_list:
                    self.outputs_list[x] = 0.1 
            else:
                pass  
        
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

app = cocktailapp(input_nodes, hidden_nodes, output_nodes, learning_rate, path_to_trainingsdata, training_epoch, path_to_debugdata, debug_mode, serverip, port)
app.waitfordata()
#app.firsttrain()
#app.chkdebug()
