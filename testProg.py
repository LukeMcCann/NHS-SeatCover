import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Setup Outputs
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

#Setup Inputs
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)

#Configure output power
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.OUT)
GPIO.output(12,GPIO.OUT)
GPIO.output(16,GPIO.OUT)
GPIO.output(18,GPIO.OUT)

currentInput = 0

def mainFunction(inChannel, outChannel):
    if(GPIO.input(inChannel) == True):
        if(currentInput == 0):
            currentInput = 1
            GPIO.output(outChannel,GPIO.HIGH)
        elif(currentInput == 1):
            currentInput = 0
            GPIO.output(outChannel,GPIO.LOW)
    else:
        return
    
try:
    while True:
        mainFunction(3,8)
        mainFunction(5,10)
        mainFunction(7,12)
        mainFunction(11,16)
        mainFunction(13,18)
except:
    print("Error")
