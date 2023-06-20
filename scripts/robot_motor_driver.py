#!/usr/bin/env python

import time

#import motor libraries
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

#create a motorHAT object
mh = Adafruit_MotorHAT(addr=0x60)

#create DC motor objects
rightMotor = mh.getMotor(1)
leftMotor = mh.getMotor(2)

#set motor speed
rightMotor.setSpeed(200)
leftMotor.setSpeed(200)

#start motors
rightMotor.run(Adafruit_MotorHAT.FORWARD)
leftMotor.run(Adafruit_MotorHAT.FORWARD)

#run for 5 seconds
time.sleep(5)

#stop motors
rightMotor.run(Adafruit_MotorHAT.RELEASE)
leftMotor.run(Adafruit_MotorHAT.RELEASE)