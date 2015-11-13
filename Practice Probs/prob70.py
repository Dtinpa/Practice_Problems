#!/usr/bin/env python

def relative_prime(num):
	prime_list = []
	i = 1
	while i < num:
		if num%i != 0:
			prime_list.append(i)
		i += 1
	return prime_list

def is_permutation(orig_num, num):
	str_orig_num = ''.join(sorted(str(orig_num)))
	str_num = ''.join(sorted(str(num)))
	if str_orig_num == str_num:
		return True
	else:
		return False

i = 2
min = 0
prod_min = 0
while i < 10**7:
	list_prime = relative_prime(i)
	for x in list_prime:
		if is_permutation(i, x):
			if min == 0:
				min = i/x
				prod_min = i
			elif min > i/x:
				prod_min = i
				min = i/x
	i += 1

print prod_min
