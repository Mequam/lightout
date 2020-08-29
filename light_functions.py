#!/usr/bin/python3.4
#this file contains functions for manipulating gpoi lights on a raspberry
#pi using an array of light data

from gpiozero import LED
from time import sleep
from threading import Thread

#takes a pin number and causes the light on that pin to blink
def light_routine(pin_num,state,hook=lambda a : a):
	light = LED(pin_num)
	for instruction in state:
		instruction = hook(pin_num,instruction)
		update_light_state(light,instruction[0])
		sleep(instruction[1])
							

def update_light_state(light,on):
	if on:
		light.on()
	else:
		light.off()
def light_cmd_to_str(cmd):
	return ("on" if cmd[0] else "off") + " for {0} seconds".format(cmd[1])
def blink_all_lights(light_r,hook=lambda a : a):
	threads = []
	for routine in light_r:
		threads.append(Thread(target=light_routine,args=(routine[0],routine[1],hook)))
	for th in threads:
		th.start()
	for th in threads:
		th.join()	
if __name__ == '__main__':
	import light_data
	instructions = [(True,2),(False,2),(True,4),(False,0)]
	def print_inst_val(pin_num,inst):
		print("[{0}] ".format(pin_num) + light_cmd_to_str(inst))
		return inst	
	blink_all_lights([(17,instructions)],print_inst_val)
