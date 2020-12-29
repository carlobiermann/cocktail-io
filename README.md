# cocktail-io 

__DISCLAIMER:__ This project is part of an ongoing graduate course at the HTW Berlin.

## Table of Contents

- [Intro](#intro)
  * [Hardware](#hardware)
- [System workflow](#system-workflow)
- [Architecture](#architecture)

## Intro

This repository contains the software for an automated cocktailmaker which recommends a drink to the user based on the  users emotions and alcohol level using an Artificial Neural Network (ANN). 

We're planning to use 8 bottles of liquor and drinks to create 10 different types of drink recipes.

### Hardware

The cocktailmaker consists of the following hardware:
- Raspberry Pi 4 Model B + LCD Touchscreen + Pi Cam
- Arduino Mega + various sensors
- Laptop (any model)
- 8 magnetic valves

The box casing is planned to be made of sheet metal and will hold the 8 liquor and drink bottles as well as the Arduino Mega, Raspberry Pi and magnetic valves.

## System workflow

1. User is in front of the machine and is introduced to the procedure via the GUI
2. GUI leads user through every step in the process such as the 10 second emotion detection and 10 second alcohol measurement.
3. Measurement data is sent to the ANN
4. ANN processes data and outputs three  drink recommendations
5. Three drink recommendations get displayed on the GUI
6. User selects one of the three drinks 
7. Routine starts the create the selected drinks via control of the valves
8. ANN is trained with the selected drink 
9. Programm starts from the beginning.

## Architecture

Below you'll find the current architecture of the cocktailmaker and its dataflow.

![architecture](https://https://github.com/carlobiermann/cocktail-io/blob/master/pics/architecture.jpg)
