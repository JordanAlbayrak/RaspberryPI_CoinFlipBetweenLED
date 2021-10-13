from random import seed
from random import random
import RPi.GPIO as GPIO
from time import sleep

seed(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# while True:
GPIO.output(4, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
sleep(1)
GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
sleep(1)
counter = 0
while True:

    while GPIO.input(2) == GPIO.LOW:
        if counter == 0:
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.LOW)
            sleep(0.3)
            counter += 1
        elif counter == 1:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            sleep(0.3)
            counter += 1
        elif counter == 2:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(6, GPIO.HIGH)
            sleep(0.3)
            counter += 1
        elif counter == 3:
            GPIO.output(4, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.LOW)
            sleep(0.3)
            counter = 0


