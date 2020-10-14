#Kendra Ludwig (kel334@nau.edu)
#Michael Reed (msr248@nau.edu)


import random


def main():
	board = []

	randomize(board)
	moves = 0
	while not is_solved(board):
		show(board)
		(row, col) = ask_row_and_col()
		touch(board, row, col)
		moved += 1
	show(board)
	print(f"You won with {moves} moves!")

def board():
	board = [
		[X, X, X, X, X],
		[X, X, X, X, X],
		[X, X, X, X, X],
		[X, X, X, X, X],
		[X, X, X, X, X]
	]	
#replace X's with something else??
#not random here?? creates unplayable games

def ask_row_and_col():
	row = input("Please choose a row coordinate (0-4): ")
	col = input("Please choose a column coordinate (0-4): ")


def touch(board, row, col):


def is_solved():

