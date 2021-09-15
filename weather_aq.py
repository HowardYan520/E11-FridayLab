import serial
from adafruit_bme280 import basic as adafruit_bme280
import time as time
import csv
import board




## This is for the weather
from adafruit_bme280 import basic as adafruit_bme280
import board
i2c=board.I2C()
sensor=adafruit_bme280.Adafruit_BME280_I2C(i2c)
## The weather import section has ended




current_time=time.time()
run_time=10
stop_time=current_time+run_time
sleep_time=1


## This is for air quality (do NOT change)
port=serial.Serial("/dev/serial0",baudrate=9600,timeout=1.5)
## The air quality section has ended 


with open('weather_and_air.csv','w',newline='') as csvfile:
	csvwriter=csv.writer(csvfile,delimiter=',')
	
	header=['Time','PM_1','PM_2_5','PM_10','Temperature','Humidity','Pressure']
	csvwriter.writerow(header)
	
	while current_time < stop_time+run_time:
		text=port.read(32)
		PM_1=int.from_bytes(text[4:6],byteorder="big")
		PM_2_5=int.from_bytes(text[6:8],byteorder="big")
		PM_10=int.from_bytes(text[8:10],byteorder="big")
		
		## The weather data code
		temp=sensor.temperature
		humidity = sensor.relative_humidity
		pressure = sensor.pressure
		
		current_time = time.time()
		data_list=[current_time,PM_1,PM_2_5,PM_10,temp,humidity,pressure]
		csvwriter.writerow(data_list)
		print(data_list)
		time.sleep(sleep_time)

		
csvfile.close()
