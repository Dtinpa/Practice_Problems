#!/usr/bin/env python

f = open("alpha_order.txt", "r")

for line in f:
	line = line.rstrip()
	sorted_word = ''.join(sorted(line))
	reverse_sorted_word = ''.join(sorted(line, reverse=True))
	if line == sorted_word:
		print line + " IN ORDER"
	elif line == reverse_sorted_word:
		print line + " IN REVERSE ORDER"
	else:
		print line + " NOT IN ORDER"
