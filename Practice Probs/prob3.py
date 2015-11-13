#!/usr/bin/env python


def get_factors(num):
        j = 2
        factor = ""
        while j < num/2:
                if num%j == 0:
                        if j*j == num:
                                factor += get_factors(j) + "*" + get_factors(j)
                                return factor
                        else:
                                factor += get_factors(num/j) + "*" + str(j)
                                return factor
                j += 1

        if not factor:
                return str(num) + "*"


prime = get_factors(600851475143).split("*")

print prime[0]
