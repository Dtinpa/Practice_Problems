#!/usr/bin/env python

from math import cos, sin, tan,  radians

dottie_cos = 5.0
dottie_tan = 2.0
dottie_fixed = 1.0
dottie_wut = 0.5

num_string_cos = "0"
num_string_tan = "0"
num_string_fixed = "0"
num_string_wut = "0"

while abs(float(num_string_cos) - dottie_cos) >= 0.000000000001:
	num_string_cos = str(dottie_cos)
	dottie_cos = cos(dottie_cos)

print dottie_cos

while abs(float(num_string_tan) - dottie_tan) >= 0.000000000001:
        num_string_tan = str(dottie_tan)
        dottie_tan = dottie_tan - tan(dottie_tan)

print dottie_tan

while abs(float(num_string_fixed) - dottie_fixed) >= 0.000000000001:
        num_string_fixed = str(dottie_fixed)
        dottie_fixed = 1 + 1/dottie_fixed

print dottie_fixed

while abs(float(num_string_wut) - dottie_wut) >= 0.000000000001:
        num_string_wut = str(dottie_wut)
        dottie_wut = 4*dottie_wut*(1 - dottie_wut)

print dottie_wut
