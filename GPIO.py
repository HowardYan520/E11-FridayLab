import RPi.GPIO as GPIO
import time 
from time import sleep 
import datetime
## Update for 10/28: write code that can create a csv file and collect data
import time 
import random
import sys
import csv

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
## This wil allow us to collect counts per minute
interval=60
sleep_time=1

print(sys.argv)
if len(sys.argv)>1:
	interval=int(sys.argv[1])
	if len(sys.argv)>2:
		sleep_time=int(sys.argv[2])
start_time=time.time()
current_time=start_time


with open('GPIO_data_kromek.csv','w',newline='') as csvfile:
	testwriter=csv.writer(csvfile,delimiter=',')
	while current_time < start_time + interval:
		Time = datetime.datetime.now()
		current_time=time.time()
		Counts= Count
		data_list=[current_time,Counts]
		testwriter.writerow(data_list)
		print("%s - Count = %6d" % (Time, Count))
		Count = 0 
		time.sleep(sleep_time)

GPIO.cleanup()

## Add additional code to write the csv file

	

