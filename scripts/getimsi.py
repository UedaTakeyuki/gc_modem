import re
import at
import argparse
import imsi_table

pattern = re.compile("(([0-9][0-9][0-9])([0-9][0-9])([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]))\r\n")

def read():
	imsi  	= ""
	mcc   	= ""
	mnc   	= ""
	carrier = ""

	lines = at.read("AT+CIMI")

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		imsi = matchOB.group(1)
		mcc  = matchOB.group(2)
		mnc  = matchOB.group(3)
		if imsi in imsi_table.imsi_table:
			carrier = imsi_table.imsi_table[imsi]["carrier"]
		elif mcc+mnc in imsi_table.mccmnc_table:
			carrier = imsi_table.mccmnc_table[mcc+mnc]["carrier"]
	return {"imsi": imsi, "mcc": mcc, "mnc": mnc, "carrier": carrier}

def carrier():
	return read()["carrier"]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Get IMSI")
	parser.add_argument("-carrier", 
		                  help='return carrier name only',
		                  action='store_true')
	args = parser.parse_args()
	if args.carrier:
		print carrier()
	else:
		print read()
