#!/usr/bin/python3

import RPi.GPIO as GPIO
import time,sys

FLOW_SENSOR = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
    count += 1
    print('revs: {}'.format(count))

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = (count * 60 * 2.25 / 1000)
        print('The flow is: {} Liter/min'.format(flow))
        count = 0
        time.sleep(3)
    except KeyboardInterrupt:
        print('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        sys.exit()
