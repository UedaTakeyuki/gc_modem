import re
import at

pattern = re.compile('^\+COPS:.*"(([0-9][0-9][0-9])([0-9][0-9]))".*\\r\\n')

def read():
	cop  = ""
	mcc  = ""
	mnc  = ""

	lines = at.read("AT+COPS=3,2")
	lines = at.read("AT+COPS?")

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		cop = matchOB.group(1)
		mcc  = matchOB.group(2)
		mnc  = matchOB.group(3)
	return [cop, mcc, mnc]

if __name__ == '__main__':
	print read()