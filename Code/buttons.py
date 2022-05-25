import RPi.GPIO as GPIO
import time
import os

os.system('raspi-gpio set 19 ip')
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnOnScreen():
    os.system('raspi-gpio set 19 op a5')
    os.system('raspi-gpio set 18 op a5')
    # os.system('vcgencmd display_power 1')
    os.system('tvservice --sdtvon="NTSC [P]"')

def turnOffScreen():
    os.system('raspi-gpio set 19 ip')
    os.system('raspi-gpio set 18 ip')
    # os.system('vcgencmd display_power 0')
    os.system('tvservice -o')

turnOffScreen()
screen_on = False

while (True):
    # If you are having and issue with the button doing the opposite of what you want
    # IE Turns on when it should be off, change this line to:
    # input = not GPIO.input(26)
    input = GPIO.input(26)
    if input != screen_on:
        screen_on = input
        if screen_on:
            turnOnScreen()
        else:
            turnOffScreen()
    time.sleep(0.3)
