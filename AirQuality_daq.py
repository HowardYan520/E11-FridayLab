import serial
from adafruit_bme280 import basic as adafruit_bme280
import time as time
import csv
import board

current_time=time.time()
run_time=10
stop_time=current_time+run_time
sleep_time=1

port=serial.Serial("/dev/serial0",baudrate=9600,timeout=1.5)
#csvwriter=csv.writer(csvfile,delimiter=',')
#csvfile=open('air.csv','w',newline='')

with open('air.csv','w',newline='') as csvfile:
	csvwriter=csv.writer(csvfile,delimiter=',')
	
	header=['Time','PM_1','PM_2_5','PM_10']
	csvwriter.writerow(header)
	
	while current_time < stop_time+run_time:
		text=port.read(32)
		PM_1=int.from_bytes(text[4:6],byteorder="big")
		PM_2_5=int.from_bytes(text[6:8],byteorder="big")
		PM_10=int.from_bytes(text[8:10],byteorder="big")
		current_time = time.time()
		data_list=[current_time,PM_1,PM_2_5,PM_10]
		csvwriter.writerow(data_list)
		print(data_list)
		time.sleep(sleep_time)

		
csvfile.close()


