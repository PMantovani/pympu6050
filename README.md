# pympu6050

## Introduction

An implementation in Python for communication with the MPU-6050 accelerometer/gyroscope. Perfect for Raspberry Pi.

MPU-6050 is an accelerometer and gyroscope sensor that communicates through the protocol I2C. In order to communicate properly with it, it's necessary to understand most of their registers and how to parse their bits and bytes to a result that makes sense to the users.

This library is meant to solve these issues by providing an API layer that facilitates this communication. So, instead of having to remember the register that reads the X-Axis of the accelerometer, parse the 2-compliment answer from the I2C line, and then adjusting to the scale, you can simply call the method get_accelerometer_x, for example.

Note that this library doesn't contain all the functionality that the MPU-6050 provides, but should be great for the most common tasks, such as reading the accelerometer and gyroscope values, and setting their scale.

## Wiring

The steps below refer to the wiring connections with a Raspberry Pi Model 3 B+, but this library can be used for any device that supports Python.
