import RPi.GPIO as GPIO
import time 
from time import sleep 
import datetime

def GlobalCounter(channel):
	global Count 
	
	Count += 1 
	time.sleep(0.0001)

	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#GPIO.setup(17, GPIO.OUT)
GPIO.setup(17, GPIO.IN)
GPIO.add_event_detect(17, GPIO.FALLING, callback =GlobalCounter)

Count=0


while True:
	Time = datetime.datetime.now()
	print("%s - Count = %6d RPM = %6d" % (Time, Count, Count *60))
	RPM = Count * 60
	Count = 0 
	t = time.time()
	Wait = 1 - (t- int(t))
	time.sleep(Wait)

GPIO.cleanup()

	

