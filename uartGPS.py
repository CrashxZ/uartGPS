
import serial
import os
# change "/dev/ttyTHS0" to your device address (Check with dmesg)
# change the baudrate as required 
# timeout in seconds
gps = serial.Serial("/dev/ttyTHS0", baudrate=57600, timeout=1)
while gps.is_open:
	input = gps.readline()
	print input

	

