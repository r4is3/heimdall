#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

This file is part of Heimdall.

Heimdall is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Heimdall is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Heimdall.  If not, see <http://www.gnu.org/licenses/>. 

Authors: 
- Vandecappelle Steeve<svandecappelle@vekia.fr>
- Sobczak Arnaud<asobczack@vekia.fr>

# Name:         heimdall.py
# Author:       Vandecappelle Steeve & Sobczak Arnaud
# Copyright:    (C) 2013-2014 Vandecappelle Steeve & Sobczak Arnaud
# Licence:      GNU General Public Licence version 3
# Website:      http://vekia.github.io/heimdall/
# Email:        svandecappelle at vekia.fr
"""

import sys
from lib.utils.Logger import Logger
from runner.DatabaseAccessor import Accessor

if __name__ == '__main__':
	if sys.version_info >= (3, 0):
		print("\nThis is the Python 2 version of Python, but you are " + 
			"running it with Python 3 or newer!\n\n")
	else:
		if sys.version_info < (2, 6):
			print("\n" + 
			"********************************************************\n" + 
			"WARNING:\n" + 
			"This version of Python was designed for " + 
			"Python 2.6 or greater.\n" + 
			"Your version of Python is older, so this is unlikely " + 
			"to work!\n\n" + 
			"But lets see how far we get...\n" + 
			"********************************************************\n")


	
	logger = Logger("Runner")
	logger.debug("Database access changer started")
	accessor = Accessor()
	accessor.start()
	
