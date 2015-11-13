#!/usr/bin/env python

f = open("moves.txt")

play_grid = [[]]*6

j = 0
while j < len(play_grid):
	play_grid[j] = ["-"]*7
	j += 1
	

play_grid_column_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def make_move(col, piece):
	col_selected = play_grid_column_letters.index(col)
	i = len(play_grid) - 1
	while i > 0:
		if play_grid[i][col_selected] == "-":
			play_grid[i][col_selected] = piece
			return has_won(i, col_selected, piece)
		i -= 1

def has_won(row, col, piece):
	win = ""
	
	win = test_col_win(row, col, piece, 0)

	if win == "":
		win = test_row_win(row, col, piece, 0)
	if win == "":
		win = test_left_diag_win(row, col, piece, 0)
	if win == "":
		win = test_right_diag_win(row, col, piece, 0)

	return win

def test_col_win(row, col, piece, count):
	i = 0
	combo = ""
	row_len = len(play_grid)
	while i < row_len:
		if play_grid[i][col] == piece:
			count += 1
			combo += " " + play_grid_column_letters[col] + str(i)
		elif count < 4:
			count = 0
			combo = ""
		i += 1

	if count >= 4:
		return combo
	else:
		return ""

def test_row_win(row, col, piece, count):
	i = 0
	combo = ""
	col_len = len(play_grid[row])
	while i < col_len:
		if play_grid[row][i] == piece:
			count += 1
			combo += " " + play_grid_column_letters[i] + str(row)
		elif count < 4:
			count = 0
			combo = ""
		i += 1

	if count >= 4:
		return combo
	else:
		return ""

def test_left_diag_win(row, col, piece, count):
	i = 0
	combo = ""
	col_len = len(play_grid[row])
	row_len = len(play_grid)

	while row > 0 and col > 0:
		row -= 1
		col -= 1

	while row + i < row_len and col + i < col_len:
		if play_grid[row + i][col + i] == piece:
			count += 1
			combo += " " + play_grid_column_letters[col + i] + str(row + i)
		elif count < 4:
			count = 0
			combo = ""
		i += 1

	if count >= 4:
		return combo
	else:
		return ""

def test_right_diag_win(row, col, piece, count):
        i = 0
	combo = ""
	col_len = len(play_grid[row])
	row_len = len(play_grid)

	while row > 0 and col < col_len - 1:
		row -= 1
		col += 1

	while row + i < row_len and col - i > 0:
		if play_grid[row + i][col - i] == piece:
			count += 1
			combo += " " + play_grid_column_letters[col - i] + str(row + i)
		elif count < 4:
			count = 0
			combo = ""
		i += 1

	if count >= 4:
		return combo
	else:
		return ""

P1 = ""
P2 = ""
move = 1
for line in f:
	P1 = line.split(" ")[0]
	P2 = line.split(" ")[1].rstrip()

	did_win = make_move(P1.lower(), "X")

	if did_win != "":
		print "X won at move " + str(move) + " with:" + did_win
		break
	did_win = make_move(P2, "O")
	if did_win != "":
                print "O won at move " + str(move) + " with:" + did_win
                break
	move += 1
