#!/usr/bin/python3.4

#this is a command line front end to some of the 
#functions defined in the other .py files

import argparse
from encoding_functions import Pstr2arr
import light_functions as lf
from sys import stdin


parser = argparse.ArgumentParser(description='Make pins on the raspberry pi emit high low values with a given encoding')

parser.add_argument('--repeat','-r',type=int,
                    help='the number of times to repeat the given patern, leave blank to loop')

parser.add_argument('--pattern','-p',
                    help='text after the data flag is used with the encoding function, leave blank for stdin')

parser.add_argument('--verbose','-v',action='store_true',
			help='tells the program wether or not to display on off data to the terminal')

args = parser.parse_args()

light_arr = Pstr2arr(args.pattern if args.pattern else stdin.read().rstrip())


def display_pin_state(pin,val):
	print('[{0}] '.format(pin) + lf.light_cmd_to_str(val))
	return val
if not args.verbose:
	display_pin_state = lambda a, b: b
#syntatic sugar
def main():
	lf.blink_all_lights(light_arr,display_pin_state)

if (args.repeat):
	for i in range(0,args.repeat):
		main()	
else:
	while True:
		main()
