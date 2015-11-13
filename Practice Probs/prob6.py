#!/usr/bin/env python

i = 1

sum_square = 0
square_sum = 0

while i < 101:
	sum_square += i**2
	square_sum += i
	i += 1

square_sum = square_sum**2

result = square_sum - sum_square

print result
