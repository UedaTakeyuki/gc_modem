# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2018 - 

"""
  get informations

  Usage: 
						import getinfos
						getinfos.infos()

	Result:
						[csq, rssi, condition]  

	Test:
						python -m getinfos [mcc]

	glossary:
						csq:  		 signal quality
						rssi: 		 Received Signal Strength Indication
						condition: Network Condition
"""

import getgmm
import getcurrentcops
import getcsq
import getimsi

def infos():
	gmm = getgmm.read()
	if gmm: # not empty
		print "[model]"
		print 'name="{}"'.format(gmm[0])
		print ""

	cop = getcurrentcops.read()
	print "[carrier]"
	print 'cop={}'.format(cop[0])
	print 'mcc={}'.format(cop[1])
	print 'mnc={}'.format(cop[2])
	print ""

	csq = getcsq.read()
	print "[CSQ]"
	print 'csq={}'.format(csq[0])
	print 'rssi={}'.format(csq[1])
	print 'condition={}'.format(csq[2])
	print ""

	imsi = getimsi.read()
	print "[IMSI]"
	for key, value in imsi.items():
		print "{}={}".format(key, value)
	print ""

if __name__ == '__main__':
	infos()
