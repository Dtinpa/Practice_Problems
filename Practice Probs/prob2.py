#!/usr/bin/env python

def fib(n, M):
	if M[n] != 0:
		return M[n]
	elif n < 2:
		return 1
	else:
		M[n] = fib(n - 1, M) + fib(n - 2, M)
		return M[n]

def fib_mem():
	Mem = [0]*100000
	num = 1
	D = 0
	even_sum = 0
	end = 4*(10**6)
	while D < end:
		D = fib(num, Mem)
		num += 1
		if D%2 == 0:
			even_sum += D
	return even_sum
result = fib_mem()
print result
	
