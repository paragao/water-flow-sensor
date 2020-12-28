#!/usr/bin/python3
from guizero import App, Text, PushButton, Picture
import RPi.GPIO as GPIO
import time,sys
import subprocess
import PIL

def water_plants():
    GPIO.output(RGPIO, GPIO.LOW)
    time.sleep(1)
    GPIO.output(RGPIO, GPIO.HIGH)
    global count
    flow = round((count / 7.5), 2)
    flow = 2
    global lastFlow
    lasttFlow = flow

def sensor_flow():
    flow = round((count / 7.5), 2) 
    flow = 1
    flow_count(flow)

def countPulse(channel):
    global count
    count += 1

def flow_count():
    global lastFlow
    global count
    #lastFlow = flow if ((lastFlow is not None) or (lastFlow is not "0")) else "0"
    flowText.value = count
    #count = 0

def take_pic():
    process = subprocess.Popen(['fswebcam', '-r 1280x720', '--png 9', '/home/pi/Desktop/image.png'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    pic.value = '/home/pi/Desktop/image.png'

global count 
global lastFlow
count = 0
lastFlow = 0
FLOW_SENSOR = 17
GPIO.cleanup
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)
RGPIO = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RGPIO, GPIO.OUT)

try: 
    app = App(title="Water plants widget", layout="grid")
    # add the parts for you app from here until app.display()
    spacerA = Text(app, text="", grid=[0,0])
    
    waterButton = PushButton(app, command=water_plants, text="Water the plants", grid=[0,1]) 
    spacerB = Text(app, text="", grid=[0,2])

    #flowText = Text(app, text="0", grid=[1,3])
    #flowMessage = Text(app, text="Amount of water used last time: ", grid=[0,3])
    #flowText.repeat(1000, flow_count)
    #spacerC = Text(app, text="", grid=[0,4])

    pic = Picture(app, image="/home/pi/Desktop/image.png", grid=[0,5,2,1])
    pic.resize(640, 480)
    pic.repeat(5000, take_pic)

    # must be the last line
    app.display()

except KeyboardInterrupt:
    GPIO.cleanup()

