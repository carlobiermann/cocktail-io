# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

import scipy.special
import numpy as np

# neural network main class
class neuralNetwork:

    #init
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate, path_to_wih, path_to_who):
        #definiton of input-, hidden- and outputnodes
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        #learningrate
        self.lr = learningrate

        #first starting weights, -0.5 till 0.5, matrices
        #self.wih = (np.random.rand(self.inodes,self.hnodes) - 0.5) #- easy, but not normal distribution in dependency of number of nodes
        #self.who = (np.random.rand(self.hnodes,self.onodes) - 0.5) #- easy, but not normal distribution in dependency of number of nodes
        self.wih = np.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        self.wih = np.zeros(self.wih.shape) 
        self.who = np.zeros(self.who.shape)

        #sigmoid function called "activation function" in NN-context
        self.activation_function = lambda x: scipy.special.expit(x)

        #paths
        self.path_to_wih = path_to_wih
        self.path_to_who = path_to_who
        pass

    #training
    def train(self, inputs_list, targets_list):
        #converting to 2D array
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        
        #signals in the hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        #signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        #signals in the output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        #signals emerging from output layer
        final_outputs = self.activation_function(final_inputs)

        #error from target and input -> weigths between hidden layer and output layer
        output_errors = targets - final_outputs
        #error from output_errors, split by weights, recombined at hidden nodes-> weigths between input and hidden layer 
        hidden_errors = np.dot(self.who.T, output_errors)

        #update the weights of links between hidden and output layer
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        #update the weights of links between hidden and output layer
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

        pass

    #query
    def query(self, inputs_list):
        #inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T

        #signals in the hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        #signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        #signals in the output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        #signals emerging from output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

    #save weigths    
    def saveweights(self):
        np.save(self.path_to_wih, self.wih)
        np.save(self.path_to_who, self.who)
        pass

    #load weights
    def loadweights(self):
        self.wih = np.load(self.path_to_wih)
        self.who = np.load(self.path_to_who)
        pass