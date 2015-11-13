#!/usr/bin/env python

def is_prime(n):
	for x in range(3, int(n**0.5)+1, 2):
		if n%x == 0:
			return False
	return True

i = 3
sum = 2
while i < 2000000:
	prime = is_prime(i);
	if prime:
		sum += i
	i += 2

print sum
	
