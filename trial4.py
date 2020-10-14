#DO NOT TURN IN
#For trying ideas that might not work


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


def ask_row_and_col():


def touch(board, row, col):


def is_solved():

