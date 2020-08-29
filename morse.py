#!/usr/bin/python3.4

#this file contains the code to covert text from stdin into the morse code representation
#represented in the pstr format
import argparse
import encoding_functions as ef
from sys import stdin
parser = argparse.ArgumentParser(description='converts a-z 0-9 to a morse code string to be run on the given light')
parser.add_argument('pinnum',type=int,
			help='The pin to output the morse code onto')
args = parser.parse_args()

print(ef.Parr2str([
	(args.pinnum,ef.str2morse(stdin.read().rstrip()))
	]))
