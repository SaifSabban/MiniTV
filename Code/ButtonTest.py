import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

prev_input = 0

while True:
  input = GPIO.input(26)
  if ((not prev_input) and input):
    print("Button pressed")
  prev_input = input
  time.sleep(0.05)