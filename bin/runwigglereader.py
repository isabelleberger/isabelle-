#!/usr/bin/env python

"""
Read a wiggle track and print out a series of lines containing
"chrom position score". Ignores track lines, handles bed, variableStep
and fixedStep wiggle lines.
"""

from __future__ import print_function

import bx.wiggle
import psyco_full

with open('dm6.27way.phastCons.wigFix') as f:

	for fields in bx.wiggle.Reader(f):
   		 print(" ".join( map( str, fields ) ))
		 break
