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


pattern = re.compile('^\+CSQ: +([0-9]+),99\\r\\n')

def read():
	csq   			= ""
	rssi  			= ""
	condition   = ""

	lines = at.read("AT+CSQ")

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		csq = matchOB.group(1)
		if csq in csq_table.t:
			[rssi, condition] = csq_table.t[csq]
	return [csq, rssi, condition]

if __name__ == '__main__':
	print read()