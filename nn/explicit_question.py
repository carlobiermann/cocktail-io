import api_client_cocktail_nn
import train_csv as namee
import time



if __name__ == "__main__":

    wfall = input("which fall do you want to test train? 1/2/3/4/5/custom: ")

    if wfall == "1":
        question = namee.fall1
    elif wfall == "2":
        question = namee.fall2
    elif wfall == "3":
        question = namee.fall3
    elif wfall == "4":
        question = namee.fall4
    elif wfall == "5":
        question = namee.fall5
    elif wfall == "6":
        question = namee.fall6
    elif wfall == "7":
        question = namee.fall7
    elif wfall == "8":
        question = namee.fall8
    elif wfall == "9":
        question = namee.fall9
    elif wfall == "0":
        question = namee.fall0
    elif wfall == "custom":
        print("Choose your stats...")
        question = [0,0,0,0,0,0]
        question[1] = int(input("Temperature 0-255:"))
        question[2] = int(input("Humidity 0-255:"))
        question[3] = int(input("Alcohol 0-255:"))
        question[4] = int(input("Distance 0-255:"))
        question[5] = int(input("Main Emotion 0-6:"))
    else:
        print("dont know what. So, choose fall1.")
        question = namee.fall1

    ran_floats = [(question[5]) for _ in range(50)]
    temp_temperature = question[1]
    print("Random Temperature:", temp_temperature)
    temp_hum = question[2]
    print("Random Humidity", temp_hum)
    temp_alc = question[3]
    print("Random Alcohol", temp_alc)
    temp_dist = question[4]
    print("Random Distance", temp_dist)

    client = api_client_cocktail_nn.nnclient("localhost", 10000)
    data_query = client.formatdata(temp_temperature, temp_hum, temp_alc, temp_dist, ran_floats)
    nnvalues = client.senddata(data_query, "query", 1024)
    time.sleep(2)
    client.senddata((question[0]), "training", 1024)