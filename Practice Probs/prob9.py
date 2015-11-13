#!/usr/bin/env python


i = 1
numerator = 7
denominator = 8
result = 0
sum = 0
while sum <= 1000:
	a = i*denominator + numerator
	b = denominator
	c = a + 2
	print a
        print b
        print c
        print " "
	sum = a + b + c
	if sum == 1000:
		result = (denom)*(b)*(c)
	
	i += 1
	denominator += 4
	numerator += 4

print result
