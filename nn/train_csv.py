import csv
import random
import time
from datetime import datetime
import main_cocktail_nn as nn
import os

#generate training data set for 17 input nodes
#[cocktail,temperature,humidity,alcohol,distance,emotions]

training_name = "auto_train.csv"

fall0 = [0,0,243,0,243,0]
fall1 = [1,27,216,27,216,6]
fall2 = [2,54,189,54,189,1]
fall3 = [3,81,162,81,162,5]
fall4 = [4,108,135,108,135,2]
fall5 = [5,135,108,135,108,4]
fall6 = [6,162,81,162,81,3]
fall7 = [7,189,54,189,54,2]
fall8 = [8,216,27,216,27,4]
fall9 = [9,243,0,243,0,1]



def generatefile(fall, cases, training_name, val_time):

    return_values = [0]

    return_values[0] = fall[0]
    temp_data = ((fall[1]/ 255.0) * 0.99) + 0.01
    hum_data = ((fall[2]/ 255.0) * 0.99) + 0.01
    alc_data = ((fall[3]/ 255.0) * 0.99) + 0.01
    dist_data = ((fall[4]/ 255.0) * 0.99) + 0.01
    emotions_data = [(fall[5]) for _ in range(50)]
    val_angry_0 = (emotions_data.count(0) / len(emotions_data)) + 0.01
    val_disgusted_1 = (emotions_data.count(1) / len(emotions_data)) + 0.01
    val_fearful_2 = (emotions_data.count(2) / len(emotions_data)) + 0.01
    val_happy_3 = (emotions_data.count(3) / len(emotions_data)) + 0.01
    val_neutral_4 = (emotions_data.count(4) / len(emotions_data)) + 0.01 
    val_sad_5 = (emotions_data.count(5) / len(emotions_data)) + 0.01
    val_surprised_6 = (emotions_data.count(6) / len(emotions_data)) + 0.01

    val_emotions_list = [val_angry_0, val_disgusted_1, val_fearful_2, val_happy_3, val_neutral_4, val_sad_5, val_surprised_6]

    #adding values to return_values in front of scaling
    for x in range(1,(nn.scale_temperature+1),1):
        return_values.append(temp_data)
    
    for x in range(1,(nn.scale_humidity+1),1):
        return_values.append(hum_data)
    
    for x in range(1,(nn.scale_alcohol+1),1):
        return_values.append(alc_data)
    
    for x in range(1,(nn.scale_distance+1),1):
        return_values.append(dist_data)
    
    for x in range(1,(nn.scale_emotions+1),1):
        return_values.extend(val_emotions_list)

    for x in range(1,(nn.scale_time+1),1):
        return_values.extend(val_time)

    if nn.random_mode == 1:
        random_list=[(random.uniform(0.1, 1)) for _ in range(nn.random_nodes)]
        return_values.extend(random_list)

    for i in range(1,(cases+1)):  
        with open(training_name, 'a', newline='') as csvsavefile:
            wr = csv.writer(csvsavefile, quoting=csv.QUOTE_NONE)
            wr.writerow(return_values)

    training_data_file = open(training_name, "r")
    training_data_list = training_data_file.readlines()
    training_data_file.close()
    print(len(training_data_list),"records in training files")
    print("proceeded ", fall)

    return (len(return_values)-1)
    

def getdate():
    #get date and time for additional data point
    now = datetime.now()

    #instance for list
    time_list_unconverted = [0, 1, 2, 3, 4, 5]
    time_list = [0, 1, 2, 3, 4, 5]

    #format: 
    time_list_unconverted[0] = int(now.strftime("%m")) #month
    time_list_unconverted[1] = int(now.strftime("%d")) #day
    time_list_unconverted[2] = int(now.strftime("%H")) #hour 24-format
    time_list_unconverted[3] = int(now.strftime("%M")) #minute
    time_list_unconverted[4] = int(now.strftime("%S")) #second 
    time_list_unconverted[5] = int(datetime.today().weekday()) #weekday, 0 monday - 6 sunday

    #scale time values from 0.01 to 1
    time_list[0] = (time_list_unconverted[0] / 12 * 0.99) + 0.01 #12 months
    time_list[1] = (time_list_unconverted[1] / 31 * 0.99) + 0.01 #31 days
    time_list[2] = (time_list_unconverted[2] / 23 * 0.99) + 0.01 #23 hours
    time_list[3] = (time_list_unconverted[3] / 59 * 0.99) + 0.01 #59 mins
    time_list[4] = (time_list_unconverted[4] / 59 * 0.99) + 0.01 #59 secods 
    time_list[5] = (time_list_unconverted[5] / 6 * 0.99) + 0.01 #6 + 1 days -> 0!

    return time_list

if __name__ == "__main__":

    try:
        os.remove(training_name)
    except OSError:
        print("No Data found.")
        pass

    val_time = getdate()

    for i in range(1,50):
        generatefile(fall0, 1, training_name, val_time)
        generatefile(fall1, 1, training_name, val_time)
        generatefile(fall2, 1, training_name, val_time)
        generatefile(fall3, 1, training_name, val_time)
        return_values_for_measurement = generatefile(fall4, 1, training_name, val_time)
        generatefile(fall5, 1, training_name, val_time)
        generatefile(fall6, 1, training_name, val_time)
        generatefile(fall7, 1, training_name, val_time)
        generatefile(fall8, 1, training_name, val_time)
        generatefile(fall9, 1, training_name, val_time)

    print("input nodes: ", return_values_for_measurement)
    print("Success! ", training_name)
    