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

1. User is in front of the machine and is __introduced__ to the procedure via the GUI.
2. __GUI leads user__ through every step in the process such as the 10 second emotion detection and 10 second alcohol measurement.
3. Measurement __data__ is sent to the __ANN__.
4. ANN __processes data__ and outputs three  __drink recommendations__.
5. Three drink recommendations get __displayed__ on the GUI.
6. User __selects one__ of the three drinks. 
7. Routine starts to __create__ the __selected drinks__ via control of the valves.
8. ANN is __trained__ with the selected drink.
9. Program starts from the __beginning__.

## Architecture

Below you'll find the current architecture of the cocktailmaker and its dataflow.

![architecture](https://github.com/carlobiermann/cocktail-io/blob/master/pics/architecture.jpg)
