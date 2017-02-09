import Adafruit_BBIO.GPIO as GPIO
import time

#Initialize all 7-segment display
LFT = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16']
ZERO = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', 'P8_17']
ONE = ['P8_12', 'P8_13']
TWO = ['P8_11', 'P8_12', 'P8_17', 'P8_15', 'P8_14']
THREE = ['P8_11', 'P8_12', 'P8_17', 'P8_13', 'P8_14']
LL = ['P9_23', 'P9_24', 'P9_11', 'P9_12', 'P9_13', 'P9_14', 'P9_15', 'P9_16'] 
SSD= ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', 'P8_17']


#Turn off all LED Lights
for i in range(0, len(LL)):
	GPIO.setup(LL[i], GPIO.OUT)
	GPIO.output(LL[i], GPIO.LOW)

#Turn off all 7 segment display 
for i in range(0, len(SSD)):
	GPIO.setup(SSD[i], GPIO.OUT)
	GPIO.output(SSD[i], GPIO.HIGH)

#Initialize input keys 
INP = ['P8_7', 'P8_8', 'P8_9', 'P8_10']
for i in range(0, len(INP)):
	GPIO.setup(INP[i], GPIO.IN)


