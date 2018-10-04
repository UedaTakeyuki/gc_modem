# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2018 - 

"""
  set visited timezone

  Usage: 
						import settimezone
						settimezon.set()

	Test:
						python -m settimezone [mcc]

	glossary:
						mcc: mobile country code
						cop: operator selection
"""

import os
import sys
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

def set():
	[cop, mcc, mnc] = getcurrentcops.read()
	if mcc in mcc_table:
		set_from_table(mcc_table[mcc])

if __name__ == '__main__':
	if len(sys.argv) == 1:
		set()
	elif sys.argv[1] in mcc_table:
		# for test
		set_from_table(mcc_table[sys.argv[1]])