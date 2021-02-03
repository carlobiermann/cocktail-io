# skript for providing the sweetspot of the system.
import api_client_cocktail_nn as client
import random
import time
import matplotlib.pyplot as plt

client = client.nnclient("localhost", 10000)

i = 0
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0

while i < 1000:
    emotion = random.randrange(7)
    ran_floats = [emotion for _ in range(50)]
    temp_temperature = random.randrange(256)
    print("Random Temperature:", temp_temperature)
    temp_hum = random.randrange(256)
    print("Random Humidity", temp_hum)
    temp_alc = random.randrange(256)
    print("Random Alcohol", temp_alc)
    temp_dist = random.randrange(256)
    print("Random Distance", temp_dist)
    temp_choose =random.randrange(10)
    print("Random Choosing", temp_choose)

    data_query = client.formatdata(temp_temperature, temp_hum, temp_alc, temp_dist, ran_floats)
    nnvalues = client.senddata(data_query, "query", 1024)
    #time.sleep(0.1)
    client.senddata(temp_choose, "training", 1024)

    nnvalues_short = nnvalues[:2]

    if 0 in nnvalues_short:
        count_0 = count_0 +1
    if 1 in nnvalues_short:
        count_1 = count_1 +1
    if 2 in nnvalues_short:
        count_2 = count_2 +1
    if 3 in nnvalues_short:
        count_3 = count_3 +1
    if 4 in nnvalues_short:
        count_4 = count_4 +1
    if 5 in nnvalues_short:
        count_5 = count_5 +1
    if 6 in nnvalues_short:
        count_6 = count_6 +1
    if 7 in nnvalues_short:
        count_7 = count_7 +1
    if 8 in nnvalues_short:
        count_8 = count_8 +1
    if 9 in nnvalues_short:
        count_9 = count_9 +1
    
    i = i+1
    print(i)

plt.plot([0,1,2,3,4,5,6,7,8,9],[count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9],"ro")
plt.ylabel('some numbers')
plt.show()