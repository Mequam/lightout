#!/usr/bin/python3.4

#this file contains the code to covert text from stdin into the morse code representation
#represented in the pstr format
import argparse
import encoding_functions as ef
from sys import stdin
parser = argparse.ArgumentParser(description='dialates the time of the given square wave')
parser.add_argument('dial',type=float,
			help='The number to dialate the square wave by')
args = parser.parse_args() 

ret_val = []
for lights in ef.Pstr2arr(stdin.read().rstrip()):
	inner_wave = []
	for wave in lights[1]:
		inner_wave.append((wave[0],wave[1]*args.dial))
	ret_val.append((lights[0],inner_wave))
print(ef.Parr2str(ret_val))
