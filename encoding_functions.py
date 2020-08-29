#!/usr/bin/python3.4
#this file contains functions used to encode data into light array blinks

#This code is written by Max M. and Mequam


#converts a letter to morese code
tomorse = {
    " " : "0000",
    "A" : "10111000",
    "B" : "111010101000",
    "C" : "11101011101000",
    "D" : "1110101000",
    "E" : "1000",
    "F" : "101011101000",
    "G" : "111011101000",
    "H" : "1010101000",
    "I" : "101000",
    "J" : "1011101110111000",
    "K" : "111010111000",
    "L" : "101110101000",
    "M" : "1110111000",
    "N" : "11101000",
    "O" : "11101110111000",
    "P" : "10111011101000",
    "Q" : "1110111010111000",
    "R" : "1011101000",
    "S" : "10101000",
    "T" : "111000",
    "U" : "1010111000",
    "V" : "101010111000",
    "W" : "101110111000",
    "X" : "11101010111000",
    "Y" : "1110101110111000",
    "Z" : "11101110101000",
    "1" : "10111011101110111000",
    "2" : "101011101110111000",
    "3" : "1010101110111000",
    "4" : "10101010111000",
    "5" : "101010101000",
    "6" : "11101010101000",
    "7" : "1110111010101000",
    "8" : "111011101110101000",
    "9" : "11101110111011101000",
    "0" : "1110111011101110111000"
}

#converts a string to a morse code string
def tocode(string):
    STR = ""
    for s in string.upper():
        STR += tomorse[s]
    return STR

#converts a morse code to the square wave format
def tosqr(morse):
    arr = []
    curr = "1"
    cont = 0
    for m in morse:
        if m != curr:
            arr += [(bool(int(curr)),cont)]
            curr = m
            cont = 1
        else:
            cont += 1
    return arr

#returns the string as a morse square wave
def str2morse(s):
	return tosqr(tocode(s))

def arr2str(arr):
	ret_val = ''
	for t in arr:
		ret_val += str(t[1])	
		if t[0]:
			ret_val += 'u'
		else:
			ret_val += 'd'
		
	return ret_val

def str2arr(string):
	ret_val = []

	#define the recursive loop
	def recursive_loop(string):	
		if (string != ''):
			u = string.find('u')
			d = string.find('d')
			
			l = (u < d or d == -1) and u != -1
			
			#the index of the point that we are targeting
			index = u*int(l)+d*int(not l) 	
			ret_val.append((l,
					float(string[0:index])
					))
			recursive_loop(string[index+1:])
	
	#start the recursive loop	
	recursive_loop(string)
	
	#return the result
	return ret_val

def Pstr2arr(pstrLst):
	ret_val = []
	for pstr in pstrLst.split(','):
		split_str = pstr.split(':')	
		ret_val.append(
			(int(split_str[0]),str2arr(split_str[1]))
			)
	return ret_val

def Parr2str(Parr):
	ret_val = ''
	for arr in Parr:
		ret_val += str(arr[0]) + ':' + arr2str(arr[1]) + ','
	return ret_val[:-1]

if __name__ == '__main__':
	print(Parr2str(Pstr2arr(input('(test pstrLst)> '))))
