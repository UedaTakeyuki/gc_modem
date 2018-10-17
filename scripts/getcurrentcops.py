import re
import at
import argparse

pattern = re.compile('^\+COPS:.*"(([0-9][0-9][0-9])([0-9][0-9]))".*\\r\\n')

def read(d, timeout):
	cop  = ""
	mcc  = ""
	mnc  = ""

	lines = at.read("AT+COPS=3,2", d, timeout)
	lines = at.read("AT+COPS?", d, timeout)

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		cop = matchOB.group(1)
		mcc  = matchOB.group(2)
		mnc  = matchOB.group(3)
	return [cop, mcc, mnc]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Get mobile network info",
																	 epilog="result: [mccmnc, mcc, mnc]")
	parser.add_argument("-d", 
		                  help='modem device like "/dev/ttyUSB0". Default is "/dev/gc_modem"',
		                  default="/dev/gc_modem")
	parser.add_argument("-timeout", 
		                  help='timeout time with modem. Default is 1',
		                  default=1)
	
	args = parser.parse_args()
	print read(args.d, int(args.timeout))