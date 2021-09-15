# For next week
# How do we save data to a file?
# Include time stamps for each data point (done)
# -- update to use python 3 version of driver


import board


from Adafruit_BME280 import * 
import basic as adafruit_bme280
sensor=BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

i2c=board.I2C()
sensor=adafruit_bme280.Adafruit_BME280_I2C(i2c)


import time 

current_time=time.time()
run_time=10
stop_time=current_time+run_time

while current_time < stop_time+run_time:
	temp=sensor.temperature
	humidity = sensor.relative_humidity
	pressure = sensor.pressure
	time = sensor.time 
	print(temp)
	timestamp=time.time()
	print(timestamp)
	time.sleep(1)
	current_time=time.time()

import csv


def store_data(temp,timestamp):
    append = [temp,timestamp]
    with open('/home/pi/E11-software/sensor_output.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(append)
    csvFile.close()



