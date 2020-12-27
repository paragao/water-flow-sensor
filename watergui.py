#!/usr/bin/python3
from guizero import App, Text, PushButton
import RPi.GPIO as GPIO
import time,sys

def water_plants():
    RGPIO = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RGPIO, GPIO.OUT)
    GPIO.output(RGPIO, GPIO.LOW)
    time.sleep(1)
    GPIO.output(RGPIO, GPIO.HIGH)
    sensor_flow
    
def sensor_flow():
    flow = round((count / 7.5), 2) 
    flowText.value = flow

def countPulse(channel):
    global count
    count += 1

def flow_count():
    countFlow = flow

try: 
    global count,flow
    count = 0
    FLOW_SENSOR = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)
    app = App(title="Water plants widget", layout="grid")
    # add the parts for you app from here until app.display()

    waterButton = PushButton(app, command=water_plants, text="Water plants", grid=[1,1])
    waterButonText = Text(app, text="Click here to water the plants", grid=[0,1])
    flowText = Text(app, text="0", grid=[1,2])
    flowMessage = Text(app, text="Amount of water used last time: ", grid=[0,2])
    flowText.repeat(1000, flow_count)

    # must be the last line
    app.display()
except KeyboardInterrupt:
    GPIO.cleanup()

