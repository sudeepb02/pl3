import Adafruit_BBIO.GPIO as GPIO
import time as t

#Initialize all 7-segment display
ZERO = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16']
ONE = ['P8_12', 'P8_13']
TWO = ['P8_11', 'P8_12', 'P8_17', 'P8_15', 'P8_14']
THREE = ['P8_11', 'P8_12', 'P8_17', 'P8_13', 'P8_14']
LL = ['P9_23', 'P9_24', 'P9_11', 'P9_12', 'P9_13', 'P9_14', 'P9_15', 'P9_16']
SSD= ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', 'P8_17']

#Function to clear display
def clear():
        for i in range(0, len(SSD)):
                GPIO.output(SSD[i], GPIO.HIGH)

#Initialize and turn off all LED Lights
for i in range(0, len(LL)):
        GPIO.setup(LL[i], GPIO.OUT)
        GPIO.output(LL[i], GPIO.LOW)

#Initialize and turn off all 7 segment display
for i in range(0, len(SSD)):
        GPIO.setup(SSD[i], GPIO.OUT)
        GPIO.output(SSD[i], GPIO.HIGH)

#Initialize input keys
INP = ['P8_7', 'P8_8', 'P8_9', 'P8_10']
for i in range(0, len(INP)):
        GPIO.setup(INP[i], GPIO.IN)

#Set the current floor number
currFloor = 'P8_9'
prevFloor = 'P8_9'


while(True):
        #Idf ground floor key is pressed
        if(GPIO.input('P8_10')==0):
                clear()
                prevFloor = currFloor
                currFloor = 'P8_10'
                for i in range(0, len(ZERO)):
                        GPIO.output(ZERO[i], GPIO.LOW)

        #If first floor key is pressed
        if(GPIO.input('P8_8')==0):
                clear()
                prevFloor = currFloor
                currFloor = 'P8_8'
                for i in range(0, len(ONE)):
                        GPIO.output(ONE[i], GPIO.LOW)

        #If second floor key is pressed
        if(GPIO.input('P8_9')==0):
                clear()
                prevFloor = currFloor
                currFloor = 'P8_9'
                for i in range(0, len(TWO)):
                        GPIO.output(TWO[i], GPIO.LOW)

        #If THIRD floor key is pressed
        if(GPIO.input('P8_7')==0):
                clear()
                prevFloor = currFloor
                currFloor = 'P8_7'
                for i in range(0, len(THREE)):
                        GPIO.output(THREE[i], GPIO.LOW)