# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2018 - 

import sys
import serial
import argparse

def read(at_command, device="/dev/gc_modem", timeout_time=0.1):
	result = []
	s = serial.Serial(device, timeout = timeout_time)
	s.write(at_command + '\r\n')
	line = s.readline()
	while line != "":
		result.append(line)
		line = s.readline()
	# result.append(line)
	return result

if __name__ == '__main__':
	# refer https://www.yoheim.net/blog.php?q=20160509
	parser = argparse.ArgumentParser(description="AT command interface")
	parser.add_argument("at_command", 
		                  help="AT command string.")
	parser.add_argument("-d", 
		                  help='modem device like "/dev/ttyUSB0". Default is "/dev/gc_modem"',
		                  default="/dev/gc_modem")
	parser.add_argument("-timeout", 
		                  help='timeout time with modem. Default is 1',
		                  default=1)
	
	args = parser.parse_args()
	print args.at_command
	print args.d
	print args.timeout

	print read(args.at_command, args.d, int(args.timeout))
