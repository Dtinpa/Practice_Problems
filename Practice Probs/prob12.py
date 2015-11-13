#!/usr/bin/env python

def get_factors(num):
        j = 1
        factor = ""
        while j <= num**2:
                if num%j == 0:
                        factor += str(j) + "*"
                j += 1
	factors = factor.split("*")
	i = 0
	while i < len(factors):
		if factors[i] != "":
			multiple =str(num/int(factors[i]))
			if multiple in factors:
				return factor
			factor += multiple + "*"
		i += 1
	return factor

i = 2
triangle = 1
divisors = 0
while divisors < 500:
	factors = get_factors(triangle).split("*")
	divisors = len(factors) - 1
	print divisors
	triangle += i
	i += 1

print triangle
