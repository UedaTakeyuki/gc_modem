# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2018 - 

"""
  get gmm

  Usage: 
						import getgmm
						getgmm.read()

	Result:
						[gmm]  

	Test:
						python -m getgmm

	glossary:
						gmm:  		 manufacturer specific model identity. In short, model name.

"""

import re
import at
import csq_table


pattern = re.compile('^(.*)\\r\\n')

def read():
	gmm   			= ""

	lines = at.read("AT+GMM")

	matchOB = re.match(pattern, lines[1])

	if matchOB:
		gmm = matchOB.group(1)
	return [gmm]

if __name__ == '__main__':
	print read()