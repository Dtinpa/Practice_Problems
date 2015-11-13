#!/usr/bin/env python


def get_factors(num):
	j = num/2
	factor = ""
	while j > 1:
		if num%j == 0:
			if j*j == num:
				factor += get_factors(j) + "*" + get_factors(j)
				return factor
			else:
				factor += get_factors(j) + "*" + str(num/j)
				return factor
		j -= 1

	if not factor:
		return str(num) + "*"
i = 2
prime_list = {}
prime_list_max = {}

while i < 21:
	factors = get_factors(i)
	factor_array = factors.split("*")
	for k in factor_array:
		if k != "":
			if k in prime_list:
				prime_list[k] += 1
			else:
				prime_list[k] = 1

	if not prime_list_max:
		prime_list_max = prime_list
	else:
		for g in prime_list:
			if g in prime_list_max:
				if prime_list[g] > prime_list_max[g]:
					prime_list_max[g] = prime_list[g]
			else:
				prime_list_max[g] = prime_list[g]

	i += 1
	prime_list = {}

result = 1
for h in prime_list_max:
	prime = int(h)
	prime_val = prime**prime_list_max[h]

	result *= prime_val

print result
