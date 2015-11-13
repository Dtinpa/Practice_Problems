#!/usr/bin/env python

import sys

num_of_frac = int(sys.argv[1])
frac = sys.argv[2:(num_of_frac + 2)]

i = 0

while i < len(frac) - 1:
	numer = ""
	denom = ""
	new_frac = ""
	numer1 = frac[i].split("/")[0]
	numer2 = frac[i + 1].split("/")[0]
	denom1 = frac[i].split("/")[1]
	denom2 = frac[i + 1].split("/")[1]

	if denom1 == denom2:
		numer = int(numer1) + int(numer2)
		numer = numer
		denom = int(denom1)
	else:
		numer1 = int(numer1)*int(denom2)
		numer2 = int(numer2)*int(denom1)
		denom = int(denom1)*int(denom2)
		numer = numer1 + numer2

	a, b = numer, denom
	while b != 0:
		a, b = b, a%b

	numer = numer/a
	denom = denom/a
	new_frac = str(numer) + "/" + str(denom)
	frac.pop(0)
	frac[0] = new_frac

if(frac[0].split("/")[0] == frac[0].split("/")[1]):
	frac[0] = frac[0].split("/")[0]

print frac[0]





