RED_PIN   = 17
GREEN_PIN = 22
BLUE_PIN  = 24

# Number of color changes per step (more is faster, less is slower).
# You also can use 0.X floats.
#STEPS     = 1

###### END ######




import os
import subprocess
import sys
import termios
import tty
import pigpio
import time

bright = 255
r = 255.0
g = 0.0
b = 0.0
steps = 1

brightChanged = False
abort = False
state = True	#boolean if light show is on or paused

try:
	pid = subprocess.check_output(["pgrep", "pigpio"])
	print("pid:", pid)

except:
	print('Error --> Start pipiod process')
	os.system('sudo pigpiod')
	time.sleep(1)

pi = pigpio.pi()

#preparing and starting pigpiod service


def setLights(pin, brightness):
	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness) #Set value of the port --> e.g. pigpio pigs p 17 255

b = 255

#set init values for LEDs
setLights(RED_PIN, r)
setLights(GREEN_PIN, g)
setLights(BLUE_PIN, b)

time.sleep(10000)


	
print ("Aborting...")

setLights(RED_PIN, 0)
setLights(GREEN_PIN, 0)
setLights(BLUE_PIN, 0)

time.sleep(0.5)

pi.stop()#Stop "pigpio.pi()" - Process
