#!/usr/bin/env python

import sys

word = sys.argv[1]
found = False
degree = 0
duplicate_word = word[1:]
search_string = "";

for letter in word:
	j = len(duplicate_word)
	while j > 0:
		if letter == duplicate_word[j-1]:
			found = True
		j -= 1

	duplicate_word = duplicate_word[1:]
	if found:
		search_string += letter
	else:
		break
	found = False

exists = word.endswith(search_string)

if exists:
	degree = len(search_string)

print degree
		

