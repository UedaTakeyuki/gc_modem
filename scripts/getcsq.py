# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2018 - 

"""
  get csq

  Usage: 
						import getcsq
						getcsq.read()

	Result:
						[csq, rssi, condition]  

	Test:
						python -m getcsq [mcc]

	glossary:
						csq:  		 signal quality
						rssi: 		 Received Signal Strength Indication
						condition: Network Condition
"""

import re
import at
import csq_table
import argparse

pattern = re.compile('^\+CSQ: +([0-9]+),99\\r\\n')

def read(d, timeout):
	csq   			= ""
	rssi  			= ""
	condition   = ""

	lines = at.read("AT+CSQ", d, timeout)

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		csq = matchOB.group(1)
		if csq in csq_table.t:
			[rssi, condition] = csq_table.t[csq]
	return [csq, rssi, condition]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="3g signal quality",
		                               epilog="result: [csq, rssi, condition]")
	parser.add_argument("-d", 
		                  help='modem device like "/dev/ttyUSB0". Default is "/dev/gc_modem"',
		                  default="/dev/gc_modem")
	parser.add_argument("-timeout", 
		                  help='timeout time with modem. Default is 1',
		                  default=1)
	
	args = parser.parse_args()
	print read(args.d, int(args.timeout))