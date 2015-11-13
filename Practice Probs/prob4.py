#!/usr/bin/env python

i = 100
j = 100
max = 0

while i < 1000:
	while j < 1000:
		product = i*j
		prod_str = str(product)
		prod_len = len(prod_str)

		prod_begin = prod_str[0:(prod_len/2)]
		prod_end = prod_begin[::-1]

		if prod_str.endswith(prod_end):
			prod_num = int(prod_str)
			if prod_num > max:
				max = prod_num
		j += 1
	i += 1
	j = 100

print max
