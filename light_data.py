#!/usr/bin/python3.4

#this file contains classes and data that are used
#for the light encoding program for the raspberry pi

import enum

#represents a light command, on off or die to indicate stoping
class l_cmd(enum.IntEnum):
	on = 1
	off = 0	
	def to_str(l_cmd_val):
		return ["off","on"][l_cmd_val]  
class l_cmd_a:
	def __init__(self,lc,a):	
		self.sleep_time = a
		self.light_cmd = lc
	def __str__(self):		
		return "turn {0} for {1} seconds".format(l_cmd.to_str(self.light_cmd),self.sleep_time)
if __name__ == '__main__':
	print(type(l_cmd.off))
	test = l_cmd_a(l_cmd.off,2)
	print(test)	
