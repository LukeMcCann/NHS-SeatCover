import RPi.GPIO as GPIO
import time

#Initial Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup Outputs
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

#Setup Inputs
GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Configure output power
GPIO.output(8,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.output(12,GPIO.LOW)
GPIO.output(16,GPIO.LOW)
GPIO.output(18,GPIO.LOW)

currentInput = 0

def mainFunction(inChannel, outChannel):
    if(GPIO.input(inChannel) == True):
    	print("Curent Channels: " + inChannel + ":" + outChannel)
        if(currentInput == 0):
            currentInput = 1
            GPIO.output(outChannel,GPIO.HIGH)
            print("LED: ON")
            time.sleep(5)
            GPIO.output(outChannel,GPIO.LOW)
            print("LED: OFF")
        elif(currentInput == 1):
            currentInput = 0
            GPIO.output(outChannel,GPIO.LOW)
            print("LED: OFF")
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
    print("Error, no input signal")
