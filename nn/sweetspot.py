# skript for providing the sweetspot of the system.
import api_client_cocktail_nn as client
import random
import time
import matplotlib.pyplot as plt
import main_cocktail_nn as cocktail_nn
from threading import Thread
import subprocess


#list format
#scale_temperature, scale_humidity, scale_alcohol, scale_distance, scale_emotions, scale_time, scale_hidden_nodes_in_percent, learning_rate, training_epoch, path_to_debugdata, debug_mode, serverip, port
Net = "Net 17/12/10 LR 0.25 Highest"
port = 10000
inrange = 1000

# list1 = [1,1,1,1,1,1,100,0.1,1,"",0,"localhost",port]

# def nn1():    
    #nn1 = cocktail_nn.main(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10],list1[11],list1[12])

def clientfirst(port, net):

    client1 = client.nnclient("localhost", port)

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

    while i < inrange:
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

        data_query = client1.formatdata(temp_temperature, temp_hum, temp_alc, temp_dist, ran_floats)
        nnvalues = client1.senddata(data_query, "query", 1024)
        time.sleep(0.1)
        client1.senddata(temp_choose, "training", 1024)

        nnvalues_short = nnvalues[:3]

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
    plt.ylabel(net)
    plt.show()

    # print("1-0:", (count_0/inrange))
    # print("1-1:", (count_1/inrange))
    # print("1-2:", (count_2/inrange))
    # print("1-3:", (count_3/inrange))
    # print("1-4:", (count_4/inrange))
    # print("1-5:", (count_5/inrange))
    # print("1-6:", (count_6/inrange))
    # print("1-7:", (count_7/inrange))
    # print("1-8:", (count_8/inrange))
    # print("1-9:", (count_9/inrange))


    # client1 = client.nnclient("localhost", port)

    # i = 0
    # count_0 = 0
    # count_1 = 0
    # count_2 = 0
    # count_3 = 0
    # count_4 = 0
    # count_5 = 0
    # count_6 = 0
    # count_7 = 0
    # count_8 = 0
    # count_9 = 0

    # while i < inrange:
    #     emotion = random.randrange(7)
    #     ran_floats = [emotion for _ in range(50)]
    #     temp_temperature = random.randrange(256)
    #     print("Random Temperature:", temp_temperature)
    #     temp_hum = random.randrange(256)
    #     print("Random Humidity", temp_hum)
    #     temp_alc = random.randrange(256)
    #     print("Random Alcohol", temp_alc)
    #     temp_dist = random.randrange(256)
    #     print("Random Distance", temp_dist)
    #     temp_choose =random.randrange(10)
    #     print("Random Choosing", temp_choose)

    #     data_query = client1.formatdata(temp_temperature, temp_hum, temp_alc, temp_dist, ran_floats)
    #     nnvalues = client1.senddata(data_query, "query", 1024)
    #     time.sleep(0.1)
    #     client1.senddata(temp_choose, "training", 1024)

    #     nnvalues_short = nnvalues[:2]

    #     if 0 in nnvalues_short:
    #         count_0 = count_0 +1
    #     if 1 in nnvalues_short:
    #         count_1 = count_1 +1
    #     if 2 in nnvalues_short:
    #         count_2 = count_2 +1
    #     if 3 in nnvalues_short:
    #         count_3 = count_3 +1
    #     if 4 in nnvalues_short:
    #         count_4 = count_4 +1
    #     if 5 in nnvalues_short:
    #         count_5 = count_5 +1
    #     if 6 in nnvalues_short:
    #         count_6 = count_6 +1
    #     if 7 in nnvalues_short:
    #         count_7 = count_7 +1
    #     if 8 in nnvalues_short:
    #         count_8 = count_8 +1
    #     if 9 in nnvalues_short:
    #         count_9 = count_9 +1
        
    #     i = i+1
    #     print(i)

    # plt.plot([0,1,2,3,4,5,6,7,8,9],[count_0, count_1, count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9],"ro")
    # plt.ylabel(net)
    # plt.show()

    # print("1-0:", (count_0/inrange))
    # print("1-1:", (count_1/inrange))
    # print("1-2:", (count_2/inrange))
    # print("1-3:", (count_3/inrange))
    # print("1-4:", (count_4/inrange))
    # print("1-5:", (count_5/inrange))
    # print("1-6:", (count_6/inrange))
    # print("1-7:", (count_7/inrange))
    # print("1-8:", (count_8/inrange))
    # print("1-9:", (count_9/inrange))

# t1 = Thread(target=nn1)
# t1.start()
# time.sleep(1)
# t01 = Thread(target=clientfirst, args=(port, Net))
# t01.start()
clientfirst(port, Net)
    


