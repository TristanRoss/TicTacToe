import sys


def display_board(the_board):
	print("   0  1  2")
	for index, row in enumerate(the_board):
		print(index, row)
	print()

def win(the_board):
	# Horizontal Board
	for row in the_board:
		if len(set(row)) == 1 and row[0] != 0:
			print("Winner!")
			sys.exit()

board = [[1, 2, 0],
		 [2, 2, 2],
		 [2, 2, 2]]

display_board(board)
win(board)


