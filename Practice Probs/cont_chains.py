#!/usr/bin/env python

from chainLink import chainLink

f = open("cont_chains.txt", "r")

dimensions = f.readline()
height = int(dimensions.split(" ")[0])
len = int(dimensions.split(" ")[1])

def findChain(chains):
	count = 0
	i = 0
	while i < height:
		j = 0
		while j < len:
			if chains[i][j].value() == "x":
				if chains[i][j].read() == "":
					count += 1
					chains[i][j].setRead("Read")
					chains = DFS(chains, i, j)
			j += 1
		i += 1

	return count

def DFS(chainz, row, col):
	chains = chainz
	if col + 1 < len and chains[row][col + 1].value() == "x":
		if chains[row][col + 1].read() == "":
			chains[row][col + 1].setRead("Read")
			chains = DFS(chains, row, col + 1)
	if col - 1 >= 0 and chains[row][col - 1].value() == "x":
                if chains[row][col - 1].read() == "":
                        chains[row][col - 1].setRead("Read")
                        chains = DFS(chains, row, col - 1)
	if row + 1 < height and chains[row + 1][col].value() == "x":
                if chains[row + 1][col].read() == "":
                        chains[row + 1][col].setRead("Read")
                        chains = DFS(chains, row + 1, col)
	return chains

grid = []
for line in f:
	line = line.rstrip("\n")
	line_list = list(line)
	i = 0

	while i < len:
		line_list[i] = chainLink(line_list[i], "")
		i += 1
	i = 0

	grid.append(line_list)

chainz = findChain(grid)

print chainz
