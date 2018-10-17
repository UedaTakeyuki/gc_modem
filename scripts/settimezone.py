# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2018 - 

"""
  set visited timezone

  Usage: 
						import settimezone
						settimezon.set([d],[timeout])
				or
						python -m settimezone [-d=modem_device] [-timeout=modem_connection_timeouttime]

	Test:
						python -m settimezone -mcc=mcc

	glossary:
						mcc: mobile country code
						cop: operator selection
"""

import os
import sys
import argparse
import getcurrentcops

mcc_table = {}
mcc_table["414"] = {"Name": "Myanmar"	, "Area": "Asia", 	"Location": "Yangon"}
mcc_table["440"] = {"Name": "Japan"		, "Area": "Asia", 	"Location": "Tokyo"}
mcc_table["608"] = {"Name": "Senegal"	, "Area": "Africa", "Location": "Dakar"}

def set_tz(Area, Location):
	os.unlink("/etc/localtime")
	os.symlink('/usr/share/zoneinfo/{}/{}'.format(Area, Location), "/etc/localtime")

def set_from_table(table):
	set_tz(table["Area"], table["Location"])

def set(d, timeout):
	[cop, mcc, mnc] = getcurrentcops.read(d, timeout)
	if mcc in mcc_table:
		set_from_table(mcc_table[mcc])

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Set device timezone MCC(Mobile Country Code) which 3G Dongle detect")
	parser.add_argument("-d", 
		                  help='modem device like "/dev/ttyUSB0". Default is "/dev/gc_modem"',
		                  default="/dev/gc_modem")
	parser.add_argument("-timeout", 
		                  help='timeout time with modem. Default is 1',
		                  default=1)
	parser.add_argument("-mcc", 
		                  help='force set timezone as specified as mcc, for test of mcc_table',
		                  default="")
	args = parser.parse_args()
	args = parser.parse_args()
	if args.mcc:
		set_from_table(mcc_table[args.mcc])
	else:
		set(args.d, int(args.timeout))