#!/usr/bin/env python

limit = 10 ** 11
limit = limit ** 1/2
i = 0

while i < limit:
	reverse = str(i)[::-1]
	reverse_int = int(reverse)
	
	if reverse_int % 7 == 0:
		print i

	i += 7
