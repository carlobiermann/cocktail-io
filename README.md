## COCKTAIL I/O 

DISCLAIMER: This repository is part of an ongoing semester group project at the HTW Berlin.

A system that reads camera and sensor inputs from a Raspberry Pi 4 B and an Arduino.
Both devices will be connected via I2C and will provide data inputs for a neural network. 

The aim is to give the user a *drink recommendation* based on their facial expression data (read: current 
emotion) from the Pi Cam  and other analog sensors connected to the Arduino. 

Emotion and sensor data will then be send to a neural network located on a computer via the Wi-Fi protocol.

The output of the neural network is a drink recipe which the user will decide on whether they'll choose it or not. Their 
choice will also be fed back into the neural network, improving its algorithm.

Ultimately, the users *drink choice* will trigger the *drink mixing routine* which is controlled by the arduino and its connected valves.

