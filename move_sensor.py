#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime

# BCM GPIO-Referenen verwenden (anstelle der Pin-Nummern)
# und GPIO-Eingang definieren
GPIO.setmode(GPIO.BCM)
GPIO_PIR = 21

print "PIR-Modul gestartet (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

# Initialisierung
Read  = 0
State = 0

print "Warten, bis PIR im Ruhezustand ist ..."

# Schleife, bis PIR == 0 ist
while GPIO.input(GPIO_PIR) != 0:
  time.sleep(1)
print "Bereit..."

# Callback-Funktion
def MOTION(PIR_GPIO):
  print "%s - Bewegung erkannt!" % datetime.datetime.now()

print "%s - Warten auf Bewegung" % datetime.datetime.now()

try:
  # Ereignis definieren: steigende Flanke
  GPIO.add_event_detect(GPIO_PIR, GPIO.RISING, callback=MOTION)
  # laenger schlafen - Callback wird durch die Flanke aktiviert
  while True:
    time.sleep(100)

except KeyboardInterrupt:
  # Programm beenden
  print "Ende..."
  GPIO.cleanup()