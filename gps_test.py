import gps 


session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
	try:
		report = session.next()
		if report['class'] == 'TPV':
			if hasattr(report, 'time'):
				print(report.time)
			if hasattr(report, 'lat'):
				print(report.lat)
			if hasattr(report, 'lon'):
				print(report.lon)	
		print(report)
				
	except KeyError:
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None 
		print("GPS has terminated")
	
