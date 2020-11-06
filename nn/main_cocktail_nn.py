# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

## Define the NN ##
input_nodes = 784
hidden_nodes = 100
output_nodes = 10
learning_rate  = 0.3

path_to_trainingsdata = "mnist_dataset/mnist_train_100.csv"

##########################################################

import body_cocktail_nn as nn
import numpy as np 

class nninstall:

    #init
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate, path_to_trainingsdata):
        #installing new nn
        global n
        n = nn.neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)
        

        #variables 
        self.int_data_path = path_to_trainingsdata
        self.oonodes = output_nodes

        #says done, debugging
        print("Put up Neuronal Net Body...") 
        pass 
    
    #train new nn with data
    def firsttrain(self):
        #load the nn training data
        self.training_data_file = open(self.int_data_path, "r")
        self.training_data_list = self.training_data_file.readlines()
        self.training_data_file.close()

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
            n.train(self.inputs, self.targets)

        #says done, debugging
        print("Neuronal net ready.")
        pass

class cocktailapp:

    def __init__(self):
        #TO-DO: socket Server
        pass

    def waitfordata(self):
        #TO-DO: socket loop to get data

        ################################
        # input format for data:
        #  list! between 0 and 255
        ################################ 

        self.scaled_input = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        print(scaled_input)
        pass
    
    def rektrain(self):
        #TO-DO: train funktion activ net
        #To-DO: write to nn trainingdata set
        pass

    def query(self):
        pass

    def chkdebug(self):
        self.test_data_file = open("mnist_dataset/mnist_test_10.csv", "r")
        self.test_data_list = self.test_data_file.readlines()
        self.test_data_file.close()

        self.all_values = self.test_data_list[0].split(",")
        print(self.all_values[0])
        self.a = n.query((np.asfarray(self.all_values[1:]) / 255.0 * 0.99) + 0.01)
        print(self.a)

nni = nninstall(input_nodes, hidden_nodes, output_nodes, learning_rate, path_to_trainingsdata)
nni.firsttrain()
app = cocktailapp()
app.chkdebug()

#testdaten zum überprüfe