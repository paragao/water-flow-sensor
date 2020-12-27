#!/usr/bin/python3

import RPi.GPIO as GPIO
import time,sys

FLOW_SENSOR = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count,loop
count = 0
loop = 0
RGPIO = 27

def countPulse(channel):
    global count
    count += 1

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = round((count / 7.5), 2)
        print('The flow is: {} Liter/min'.format(flow))
        count = 0 # every second we output the flow and zero the counter
        loop += 1

        if ((loop % 10) == 0):
            GPIO.setup(RGPIO, GPIO.OUT)
            GPIO.output(RGPIO, GPIO.LOW)
            time.sleep(1)
            GPIO.output(RGPIO, GPIO.HIGH)
            
    except KeyboardInterrupt:
        print('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        sys.exit()
