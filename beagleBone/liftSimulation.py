import Adafruit_BBIO.GPIO as g
import time as t

//Define led, buttons and ssd

upled = ['P9_11', 'P9_13', 'P9_15', 'P9_23']
downled = ['P9_12', 'P9_14', 'P9_16', 'P9_24']

buttons = ['P8_7', 'P8_8', 'P8_9', 'P8_10']

ssd = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16', 'P8_17']
zero = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_15', 'P8_16']
one = ['P8_12', 'P8_13']
two = ['P8_11', 'P8_12', 'P8_17', 'P8_14', 'P8_15']
three = ['P8_11', 'P8_12', 'P8_13', 'P8_14', 'P8_17']

//Initialize 
for i in range(len(upled)):
	g.setup(upled[i], g.OUT)
	g.setup(downled[i], g.OUT)
	g.setup(buttons[i], g.IN)

	g.output(upled[i], g.LOW)
	g.output(downled[i], g.LOW)

for i in range(len(ssd)):
	g.setup(ssd[i], g.OUT)

curr = 0
dest = 0

def clearled():
	for i in range(len(ssd)):
		g.output(ssd[i], g.HIGH)

def display(x):
	clearled()

	if(x==0):
		for i in range(len(zero)):
			g.output(zero[i], g.LOW)
	elif(x==1):
		for i in range(len(one)):
			g.output(one[i], g.LOW)
	elif(x==2):
		for i in range(len(two)):
			g.output(two[i], g.LOW)
	elif(x==3):
		for i in range(len(three)):
			g.output(three[i], g.LOW)

def disp(curr, dest):
	if(curr < dest):
		for i in range(len(upled)):
			g.output(upled[i], g.HIGH)
			g.output(downled[i], g.LOW)
	
		for i in range(curr, dest + 1):
			display(i)
			t.sleep(1)

		for i in range(len(upled)):
			g.output(upled[i], g.LOW)

	elif(curr > dest):
		for i in range(len(downled)):
			g.output(downled[i], g.HIGH)
			g.output(upled[i], g.LOW)

		for i in range(curr, dest - 1 , -1):
			display(i)
			sleep(1)

		for i in range(len(downled)):
			g.output(downled[i], g.LOW)

clearled()

while True :
	if(g.input("P8_7")==0):
		curr = dest 
		dest = 3
		disp(curr, dest)
	elif(g.input("P8_9")==0):
		curr = dest
		dest = 2
		disp(curr, dest)
	elif(g.input("P8_8")==0):
		curr = dest 
		dest = 1
		disp(curr, dest)
	elif(g.input("P8_10")==0):
		curr = dest
		dest = 0
		disp(curr, dest)


