# Cocktailmaker - NN #####################################
# create by Horizontal Joghurtz ##########################
# main source: Make Your Own Neural Network Tariq Rashid #
##########################################################

import body_cocktail_nn as nn

input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate  = 0.3


n = nn.neuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate)
print("safe")

print(n.query([1.0, 0.5, -1.5]))