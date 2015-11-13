#!/usr/bin/env python

def chain(num, chain_list):
	if num == 1:
		return chain_list
	if num%2 == 0:
		return str(num/2) + " " + chain(num/2, chain_list)
	else:
		return str(3*num + 1) + " " + chain(3*num + 1, chain_list)


result = chain(13, "")

print result
