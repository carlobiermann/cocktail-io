# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

import scipy.special
import numpy as np

# neural network main class
class neuralNetwork:

    #init
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #definiton of input-, hidden- and outputnodes
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        #learningrate
        self.lr = learningrate

        #first starting weights, -0.5 till 0.5, matrices
        #self.wih = (np.random.rand(self.inodes,self.hnodes) - 0.5) - easy, but not normal distribution in dependency of number of nodes
        #self.who = (np.random.rand(self.hnodes,self.onodes) - 0.5) - easy, but not normal distribution in dependency of number of nodes
        self.wih np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        #sigmoid function called "activation function" in NN-context
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    #training
    def train():
        pass

    #query
    def query(self, inputs_list):
        #inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T

        #signals in the hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        pass 