#!/usr/bin/python3

import RPi.GPIO as GPIO
import time,sys

GPIO.setmode(GPIO.BCM)

RELAY_GPIO = 27

GPIO.setup(RELAY_GPIO, GPIO.OUT)
GPIO.output(RELAY_GPIO, GPIO.LOW)
time.sleep(3)
GPIO.output(RELAY_GPIO, GPIO.HIGH)
time.sleep(2)
GPIO.cleanup()
