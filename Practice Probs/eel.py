#!/usr/bin/env python

import sys
import re

#regex formula I used as a basis for the regex builder:
#\b[^i]*i{1}[^i]*\b

def search_reg(swear_reg, word):
	m = re.search(swear_reg, word)
	if m is not None:
		return True
	return False

f = open("eel_words.txt", "r")

slur = raw_input("Enter the slur: ")

#constructing regex pattern
slur_reg = "\\b"
slur_arr = list(slur)
for letter in slur_arr:
	slur_reg += "[^" + slur + "]*" + letter + "{1}"
slur_reg += "[^" + slur + "]*\\b"

prob_count = 0
for line in f:
	line = line.rstrip()
	if search_reg(slur_reg, line):
		print  line + " -> offensive"
		prob_count += 1

print slur + "'s problem count: " + str(prob_count)
