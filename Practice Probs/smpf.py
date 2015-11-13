#!/usr/bin/env python 

import sys

sum_up = 10 ** 12

def smpf(number):
	i = 3
	while i <= number**(1/2):
		if number%2 == 0:
			i = 2
			break
		elif number%i == 0 and i <= number:
			break
		elif i > number:
			i = 0
			break

		i += 2
	return i


sum = 0

while sum_up >= 2:
	sum += smpf(sum_up)
	sum_up -= 1

ten_to_nine = 10 ** 9
answer = sum%ten_to_nine
print answer
