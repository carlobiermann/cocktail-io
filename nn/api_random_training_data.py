# create random csv training data for cocktail to check correctly working of nn
# Horizontal Joghurtz

import random
import os
import csv

input_nodes = 89

path_to_trainingsdata = "cocktail_dataset//cocktail_training_data_random.csv"
script_dir = os.path.dirname(__file__)
int_data_path = os.path.join(script_dir, path_to_trainingsdata)

for x in range(100):
    ran_list = [random.uniform(0,1) for _ in range(input_nodes)]
    ran_list.insert(0, random.randrange(10))

    with open(int_data_path, 'a', newline='') as csvsavefile:
        wr = csv.writer(csvsavefile, quoting=csv.QUOTE_NONE)
        wr.writerow(ran_list)

    print(x)
