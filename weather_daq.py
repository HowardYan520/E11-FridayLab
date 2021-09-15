# For next week
# How do we save data to a file?
# Include time stamps for each data point (done)
# -- update to use python 3 version of driver


import board
import csv
import time as time
from adafruit_bme280 import basic as adafruit_bme280

##from Adafruit_BME280 import * 
##import basic as adafruit_bme280
## sensor=BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

i2c=board.I2C()
sensor=adafruit_bme280.Adafruit_BME280_I2C(i2c)



current_time=time.time()
run_time=10
stop_time=current_time+run_time

with open('weather.csv','w',newline='') as csvfile:
	testwriter=csv.writer(csvfile,delimiter=',')
	
	while current_time < stop_time+run_time:
		temp=sensor.temperature
		humidity = sensor.relative_humidity
		pressure = sensor.pressure
		current_time = time.time()
		testwriter.writerow([current_time,temp])
		print(current_time)
		print(temp)
		time.sleep(1)
		
csvfile.close()

##def store_data(temp,timestamp):
    ##append = [temp,timestamp]
    ##with open('/home/pi/E11-software/sensor_output.csv', 'a') as csvFile:
        ##writer = csv.writer(csvFile)
        ##writer.writerow(append)
    ##csvFile.close()



