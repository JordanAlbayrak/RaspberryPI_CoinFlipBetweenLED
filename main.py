from random import randrange
import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
sleep(1)
counter = 1
y = False
while True:
    if GPIO.input(2) == GPIO.LOW:
        y = True
        x = 0.5
        i = 0
        counter = 1
        
        
    if y == True and counter == 1:   
        if i <= x:
            GPIO.output(4, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            sleep(i)
            GPIO.output(4, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            sleep(i)
            print (i)
            i += 0.05
        elif i >= x:
            ran = randrange(2)
            print("RAN: " + str(ran))
            if ran == 0:
                GPIO.output(4, GPIO.LOW)
                GPIO.output(5, GPIO.HIGH)
            elif ran == 1:
                GPIO.output(4, GPIO.HIGH)
                GPIO.output(5, GPIO.LOW)
            counter = 0
