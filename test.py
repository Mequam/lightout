import encoding_functions as ef
import light_functions as lf

def display_pin_state(pin,val):
	print('[{0}] '.format(pin) + lf.light_cmd_to_str(val))
	return val
resp = input('(morse to repeat)> ')
while True:
	lf.blink_all_lights([(17,ef.str_morse2lights(resp))],display_pin_state)
