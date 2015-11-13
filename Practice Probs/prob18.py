#!/usr/bin/env python
# don't try to run.  Write out this function first on paper before continuing on# this problem.

def max_height(tri_array, height):
	i = 0
	j = 0
	if len(tri_array) == 1:
		return tri_array
	for x in tri_array[height - 1]:
		if int(tri_array[height][i]) > int(tri_array[height][i + 1]):
			tri_array[height - 1][j] = str(int(x) + int(tri_array[height][i]))
		elif int(tri_array[height][i]) < int(tri_array[height][i + 1]):
                        tri_array[height - 1][j] = str(int(x) + int(tri_array[height][i + 1]))  
		i += 1
		j += 1

	return max_height(tri_array[:-1], height - 1)


f = open("triangle_prob18.txt", "r")

triangle_array = []
for line in f:
	row = line.rstrip().split(" ")
	triangle_array.append(row)

height = len(triangle_array) - 1
paths = max_height(triangle_array, height)

print paths[0][0]
