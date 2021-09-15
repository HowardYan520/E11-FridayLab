import time 
import random
import sys
import csv

from adafruit_bme280 import basic as adafruit_bme280
import board
i2c=board.I2C()
sensor=adafruit_bme280.Adafruit_BME280_I2C(i2c)


interval=10
sleep_time=1


print(sys.argv)
if len(sys.argv)>1:
	interval=int(sys.argv[1])
	if len(sys.argv)>2:
		sleep_time=int(sys_argv[2])
	

start_time=time.time()
current_time=start_time

csvfile=open("Sensor_data.csv",'w',newline='')
csvwriter=csv.writer(csvfile,delimiter=',')

header=['Time','AQI']
csvwriter.writerow(header)

while current_time < start_time + interval:
	data=sensor.air_quality
	current_time=time.time()
	data_list=[current_time,data]
	csvwriter.writerow(data_list)
	print(current_time,data)
	time.sleep(sleep_time)
	
