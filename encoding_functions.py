#!/usr/bin/python3.4
#this file contains functions used to encode data into light array blinks

#converts a letter to morese code
def ltr2morse(ltr):
	return {'a':"dD",
		'b':"Dddd",
		'c':"DdDd",
		'd':"Ddd",
		'e':"d",
		'f':"ddDd",
		'g':"DDd",
		'h':'dddd',
		'i':'dd',
		'j':'dDDD',
		'k':'DdD',
		'l':'dDdd',
		'm':'DD',
		'n':'Dd',
		'o':'DDD',
		'p':'dDDd',
		'q':'DDdD',
		'r':'dDd',
		's':'ddd',
		't':'D',
		'u':'ddD',
		'v':'dddD',
		'w':'dDD',
		'x':'DddD',
		'y':'DdDD',
		'z':'DDdd'
		}[ltr]
def weve(val,arr):
	ret_val = []
	for i in arr[0:-1]:	
		ret_val.append(i)
		ret_val.append(val)
	ret_val.append(arr[-1])
	return ret_val
def add_after(to_add,arr,test_func = lambda a : True):
	ret_val = []
	for val in arr:
		ret_val.append(val)
		if (test_func(val)):
			ret_val.append(to_add)
	return ret_val
	
#takes a string and returns the morse code of that string
def str_morse2lights(string,dot_time=.5):
	def d_map(val):
		if val == 'd':
			return (True,dot_time)
		else:
			return (True,dot_time*3)
	def outer_map(val):
		return list(map(d_map,val))
	ret_val = []
	for word in string.split(' '):
		for letter in weve('_',word):
			if letter == '_':
				ret_val.append((False,dot_time*3))
			else:	
				for time in weve((False,dot_time),list(map(d_map,ltr2morse(letter)))):
					ret_val.append(time)
		ret_val.append((False,dot_time*7))
	return ret_val	
				
if __name__ == '__main__':
	print(weve('_',input('(weve test)> ')))
	str_morse2lights(input('(test)> '))	
