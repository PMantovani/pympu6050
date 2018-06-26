# pympu6050

## Introduction

An API in Python for communication with the MPU-6050 accelerometer/gyroscope. Perfect for use with Raspberry Pi.

MPU-6050 is an accelerometer and gyroscope sensor that communicates through the protocol I2C. In order to communicate properly with it, it's necessary to understand most of their registers and how to parse their bits and bytes to a result that makes sense to the users.

This library is meant to solve these issues by providing an API layer that facilitates this communication. So, instead of having to remember the register that reads the X-Axis of the accelerometer, parse the 2-compliment answer from the I2C line, and then adjusting to the scale, you can simply call the method get_accelerometer_x, for example.

Note that this library doesn't contain all the functionality that the MPU-6050 provides, but should be great for the most common tasks, such as reading the accelerometer and gyroscope values, and setting their scale.

## Wiring

The steps below refer to the wiring connections with a Raspberry Pi Model 3 B+, but this library can be used for any device that supports Python. The I2C connection consists of only two wires, SDA (Data) and SCL (Clock). These pins should connect to their correspondent in the other end. In the case of the Raspberry Pi Model 3 B+, the first I2C line is present at pins 3 and 5 (as shown in the picture below). Besides the I2C wires, it is also necessary to power up the MPU-6050 by attaching a 5V and GND lines to it. You can directly use the pins made available from the Raspberry Header Pin.

![Raspberry Pi wiring connection](https://github.com/PMantovani/pympu6050/docs/raspberry_wiring.png "Raspberry Pi Wiring Connection")

## Installing the library

So far, this code is not published in any package installer, such as PyPI, but I plan to do so soon.
Therefore, the first step should be to download the source code. Put the contents of the /src folder in the folder of your development objects.
