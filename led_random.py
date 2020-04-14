RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

import pigpio
import time
import random

bright = 255
r = 255.0
g = 0.0
b = 0.0
steps = 1

brightChanged = False
abort = False
state = True	#boolean if light show is on or paused

pi = pigpio.pi()

def setLights(pin, brightness):
	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness) #Set value of the port --> e.g. pigpio pigs p 17 255


#set init values for LEDs
setLights(RED_PIN, r)
setLights(GREEN_PIN, g)
setLights(BLUE_PIN, b)

#Main Endless Loop with Color Fading
while True:
	r = random.randrange(0, 256)
	g = random.randrange(0, 256)
	b = random.randrange(0, 256)
	setLights(RED_PIN, r)
	setLights(GREEN_PIN, g)
	setLights(BLUE_PIN, b)
	time.sleep(3)

print("Aborting")
setLights(RED_PIN, 0)
setLights(GREEN_PIN, 0)
setLights(BLUE_PIN, 0)

time.sleep(0.5)

pi.stop()#Stop "pigpio.pi()" - Process