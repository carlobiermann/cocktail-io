# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

## Define the weights / scaling of input Data in numeric parameters ##
scale_hidden_nodes_in_percent = 25

scale_temperature = 1
scale_humidity = 1
scale_alcohol = 1
scale_distance = 1
scale_emotions = 1
scale_time = 1

learning_rate  = 0.25
training_epoch = 1
debug_mode = 0

path_to_debugdata = "" #only needed for debugging

overfitting_protect = 1
overfitting_mode = "highest" # highest value stay or lowest value stay or middle value stay

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
import struct
import csv
import random

##########################################################
class cocktailapp:
    
    #init
    def __init__(self, scale_temperature, scale_humidity, scale_alcohol, scale_distance, scale_emotions, scale_time, scale_hidden_nodes_in_percent, learning_rate, training_epoch, path_to_debugdata, debug_mode):
         
        print("Starting up Cocktailmaker Engine by Horizontal Joghurtz...")

        #scaling variables
        self.scale_temp = scale_temperature
        self.scale_hum = scale_humidity
        self.scale_alc = scale_alcohol
        self.scale_dist = scale_distance
        self.scale_emo = scale_emotions
        self.scale_time = scale_time
        self.scale_hidden = scale_hidden_nodes_in_percent

        #computing params for input/hidden/outputnodes
        self.c_input_nodes = ((self.scale_temp*1)+(self.scale_hum*1)+(self.scale_alc*1)+(self.scale_dist*1)+(self.scale_emo*7)+(self.scale_time*6))
        self.c_hidden_nodes = int(self.c_input_nodes*(self.scale_hidden/100))
        if self.c_hidden_nodes < 4:
            self.c_hidden_nodes = 4 
        self.c_output_nodes = 10

        #setting up data container for these type of net
        self.string_whi = ("saved_whi_%d_%d_%d.npy" % (self.c_input_nodes, self.c_hidden_nodes, self.c_output_nodes))
        self.string_who = ("saved_who_%d_%d_%d.npy" % (self.c_input_nodes, self.c_hidden_nodes, self.c_output_nodes))
        self.string_training_data = ("cocktail_training_data_random_%d_%d_%d.csv" % (self.c_input_nodes, self.c_hidden_nodes, self.c_output_nodes))

        #other variables
        self.script_dir = os.path.dirname(__file__)
        self.path_to_debugdata = os.path.join(self.script_dir, path_to_debugdata)
        self.path_to_wih = os.path.join(self.script_dir, self.string_whi)
        self.path_to_who = os.path.join(self.script_dir, self.string_who)
        self.path_to_training_dir = os.path.join(self.script_dir, self.string_training_data)
        self.training_epoch = training_epoch
        self.debug_mode = debug_mode

        #installing new nn   
        self.n = nn.neuralNetwork(self.c_input_nodes, self.c_hidden_nodes, self.c_output_nodes, learning_rate, self.path_to_wih, self.path_to_who)

        #says done, debugging
        print("Put up Neuronal Net Body with following params...")
        print("Input Nodes:", self.c_input_nodes)
        print("Hidden Nodes:", self.c_hidden_nodes)
        print("Output Nodes:", self.c_output_nodes)

    #train new nn with data
    def firsttrain(self):
        
        #check if weights already exists
        try:
            f = open(self.path_to_wih, "r")
            f.close()
            f = open(self.path_to_who, "r")
            f.close()

        except FileNotFoundError:
            #check if training data already there
            print("No trained net matching the params of nodes found. Looking for trainingdata...")
            try:
                f = open(self.path_to_training_dir, "r")
                f.close()

            except FileNotFoundError:
                print("No trainingdata found. Generate new file with first entry...")

                for x in range(1):
                    self.ran_list_param = 1
                    self.ran_list = [random.uniform(0,1) for _ in range(self.c_input_nodes)]
                    self.ran_list.insert(0, random.randrange(10))

                    with open(self.path_to_training_dir, 'a', newline='') as csvsavefile:
                        wr = csv.writer(csvsavefile, quoting=csv.QUOTE_NONE)
                        wr.writerow(self.ran_list)

                    print(x)

                self.training_data_file = open(self.path_to_training_dir, "r")
                self.training_data_list = self.training_data_file.readlines()
                self.training_data_file.close()
                print(len(self.training_data_list),"records in training files")

            else:
                print("Load Trainingdata...")
                #load the nn training data
                self.training_data_file = open(self.path_to_training_dir, "r")
                self.training_data_list = self.training_data_file.readlines()
                self.training_data_file.close()
                print(len(self.training_data_list),"records in training files")

            #how often trainingdata were used
            print("Train new neural net...")
            for e in range(self.training_epoch):
                #loop for every record
                for record in self.training_data_list:
                    print("in loop!")
                    #record = [float(i) for i in record]
                    #format record
                    self.all_values = record.split(',')
                    self.all_values_converted = []
                
                    for element in self.all_values:
                        self.all_values_converted.append(float(element.strip('""\n')))
                    
                    #scale and shift the inputs
                    self.inputs = self.all_values_converted[1:]
                    #create the target output values (all 0.01, expect the desired label which is 0.99)
                    self.targets = np.zeros(self.c_output_nodes) + 0.01

                    #all_values[0] ist target label for this record
                    self.targets[int(self.all_values_converted[0])] = 0.99
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
    def retrain(self, data, mode):
        self.data_from_client = data
        self.trainings_mode = mode
        
        #check for debug mode
        if self.debug_mode == 0:
            
            #park the sensor data
            if (self.trainings_mode == "sensor_data"):
                self.parking_sensor_data = self.data_from_client

            #if there is a trainingvalue
            elif (self.trainings_mode == "user_input"):
                self.parking_user_input = self.data_from_client[1]
                self.parking_sensor_data.insert(0, self.parking_user_input)

                #write to training csv file
                with open(self.string_training_data, 'a', newline='') as csvsavefile:
                    wr = csv.writer(csvsavefile, quoting=csv.QUOTE_ALL)
                    wr.writerow(self.parking_sensor_data)

                #generate target list for n.train
                self.generated_target_list_from_client = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
                self.generated_target_list_from_client.insert(self.parking_user_input, 0.99)

                #train the nn 
                self.parking_sensor_data.pop(0)
                self.n.train(self.parking_sensor_data,self.generated_target_list_from_client)

            self.n.saveweights()
            pass
        else:
            pass
    
    #query for the right cocktail
    def query(self, input_list):
        
        #query the nn 
        self.input_list=input_list
        self.outputs_list = self.n.query(input_list)
        
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

def sortingdata(data, val_time, scale_temperature, scale_humidity, scale_alcohol, scale_distance, scale_emotions, scale_time):
    ################################
    # input format for data:
    # input_array[0] = 0 for syntax check
    # input_array[1] = value temperature scaled 0-255
    # input_array[2] = value alcohol scaled 0-255
    # input_array[3] = value distance scaled 0-255
    # input_array[4] = value humidity scaled 0-255
    # input_array[5...] = value emotions 0-6
    #
    # Weigth of the input params defined by user
    # -> dynamic changing of the length of return_values / input_nodes
    ################################

    #to provid a solution if emotion data is empty
    data = bytearray(data)

    if len(data) == 5:
        data.extend([1,2,3,4,5,6,0,1,2,3,4,5,6])

    #converting the input data to a value between 0.01 and 1
    temp_data = ((data[1]/ 255.0) * 0.99) + 0.01
    alc_data = ((data[2]/ 255.0) * 0.99) + 0.01
    dist_data = ((data[3]/ 255.0) * 0.99) + 0.01
    hum_data = ((data[4]/ 255.0) * 0.99) + 0.01
    emotions_data = data[5:]
    val_angry_0 = (emotions_data.count(0) / len(emotions_data)) + 0.01
    val_disgusted_1 = (emotions_data.count(1) / len(emotions_data)) + 0.01
    val_fearful_2 = (emotions_data.count(2) / len(emotions_data)) + 0.01
    val_happy_3 = (emotions_data.count(3) / len(emotions_data)) + 0.01
    val_neutral_4 = (emotions_data.count(4) / len(emotions_data)) + 0.01 
    val_sad_5 = (emotions_data.count(5) / len(emotions_data)) + 0.01
    val_surprised_6 = (emotions_data.count(6) / len(emotions_data)) + 0.01

    #packing emotion and alc data to list for multiple extend
    val_emotions_list = [val_angry_0, val_disgusted_1, val_fearful_2, val_happy_3, val_neutral_4, val_sad_5, val_surprised_6]

    #"zero-array" for the return of the values
    return_values = []
            
    #adding values to return_values in front of scaling
    for x in range(1,(scale_temperature+1),1):
        return_values.append(temp_data)
    
    for x in range(1,(scale_humidity+1),1):
        return_values.append(hum_data)
    
    for x in range(1,(scale_alcohol+1),1):
        return_values.append(alc_data)
    
    for x in range(1,(scale_distance+1),1):
        return_values.append(dist_data)
    
    for x in range(1,(scale_emotions+1),1):
        return_values.extend(val_emotions_list)

    for x in range(1,(scale_time+1),1):
        return_values.extend(val_time)

    # return_values : list with 1 element for every input_node
    return return_values

def checkiftraining(data):
    #checking if the data stream from client is training data or query data
    
    if (data[0] == 0):
        return "query"
    elif (data[0] == 1):
        return "training"
    else:
        raise Exception("cant process data from client")

#function to prevent overfitting with resetting the highest value to the next highest value
def overfitting_protection(most_signifikant_cocktails, most_signifikant_cocktails_old, output_variables_from_nn, overfitting_mode):

    #compairing the last signifikant with the next signifikant values
    samevalues = [value for value in most_signifikant_cocktails[:3] if value in most_signifikant_cocktails_old[:3]]
    
    #building up if to check if this is the same, if so, please change the highest one to the next highest and so on
    if len(samevalues) == 3:
        if overfitting_mode == "highest":
            popmodelowfirst = 1
            popmodelowsecond = 1
            popmodehighfirst = 4
            popmodehighsecond = 4

        elif overfitting_mode == "lowest":
            popmodelowfirst = 0
            popmodelowsecond = 0
            popmodehighfirst = 3
            popmodehighsecond = 3

        elif overfitting_mode == "middle":
            popmodelowfirst = 0
            popmodehighfirst = 4
            popmodelowsecond = 1
            popmodehighsecond = 4


        else:
            raise Exception("false Overfitting Mode. Typo?")
        
        most_signifikant_cocktails_overfitted = most_signifikant_cocktails

        most_signifikant_cocktails_overfitted.pop(popmodelowfirst)
        most_signifikant_cocktails_overfitted.pop(popmodelowsecond)
        most_signifikant_cocktails_overfitted.pop(popmodehighfirst)
        most_signifikant_cocktails_overfitted.pop(popmodehighsecond)  

        return most_signifikant_cocktails_overfitted  

    else:
        most_signifikant_cocktails.pop(3)
        most_signifikant_cocktails.pop(3)
        most_signifikant_cocktails.pop(6)
        most_signifikant_cocktails.pop(6)

        return most_signifikant_cocktails


##########################################################
app = cocktailapp(scale_temperature, scale_humidity, scale_alcohol, scale_distance, scale_emotions, scale_time, scale_hidden_nodes_in_percent, learning_rate, training_epoch, path_to_debugdata, debug_mode)
startingsocket(serverip, port)
app.firsttrain()
#app.chkdebug()

most_signifikant_cocktails_old = [0,0,0,0,0,0]



try:
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                print(list(data))
                
                ##############
                #main routine#
                ##############
                
                if data:
                    
                    #which data?
                    datatype = checkiftraining(data)

                    if (datatype == "query"):

                        val_time = app.getdate() 
                        input_variables_to_nn = sortingdata(data, val_time, scale_temperature, scale_humidity, scale_alcohol, scale_distance, scale_emotions, scale_time)
                        app.retrain(input_variables_to_nn, "sensor_data") 
                        output_variables_from_nn = app.query(input_variables_to_nn)
                        print("sending answer....") 
                        print(output_variables_from_nn)  
                        #answer = ("hello!".encode("utf-8"))

                        #generating a return vector
                        most_signifikant_cocktails = [0,0,0,0,0,0,0,0,0,0]

                        #get the three biggest values from nn
                        for x in range(5):
                            value_search_temp = output_variables_from_nn.max()
                            pos_search_temp = output_variables_from_nn.argmax()
                            output_variables_from_nn[pos_search_temp] = 0
                            most_signifikant_cocktails[x] = pos_search_temp
                            most_signifikant_cocktails[x+5] =  value_search_temp

                        if overfitting_protect == 1:
                            most_signifikant_cocktails = overfitting_protection(most_signifikant_cocktails, most_signifikant_cocktails_old, output_variables_from_nn, overfitting_mode)
                        elif overfitting_protect ==0:
                            most_signifikant_cocktails.pop(3)
                            most_signifikant_cocktails.pop(3)
                            most_signifikant_cocktails.pop(6)
                            most_signifikant_cocktails.pop(6)
                        else:
                            raise Exception("No Overfitting-Prevent-Mode selected.")

                        print(most_signifikant_cocktails)
                        most_signifikant_cocktails_old = most_signifikant_cocktails

                        answer = struct.pack( "<6f",*most_signifikant_cocktails)

                        print(" ")
                        print(list(answer))
                        connection.sendall(answer)

                    elif (datatype == "training"):
                        #train the nn
                        print(data)
                        app.retrain(data, "user_input")
                        connection.sendall(b"thank u")
                        pass
                    
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