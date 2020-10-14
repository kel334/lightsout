 #Kendra Ludwig (kel334@nau.edu)
 #Michael Reed (msr248@nau.edu)


import random


def main():
    white_square = "\N{WHITE SQUARE}"
    black_square = "\N{BLACK SQUARE}"
    squares = [white_square, black_square]

    board = [[random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)]]

    for row in board:
        board = row[0], row[1], row[2], row[3], row[4]
        print(row[0], row[1], row[2], row[3], row[4])

    moves = 0
    while not is_solved(board):
        show(board)
        (row, col) = ask_row_and_col()
        touch(board, row, col)
        moves += 1
    show(board)
    print(f"You won with {moves} moves!")


#def ask_row_and_col():



#def touch(board, row, col):
	if board[row][col] == white_square:
		board[row][col] = black_square
		if board[row][col+1] == white_square:
			board[row][col+1] = black_square
		elif board[row][col+1] == black_square:
			board[row][col+1] = white_square
		if board[row][col-1] == white_square:
			board[row][col-1] = black_square
		elif board[row][col-1] == black_square:
			board[row][col-1] = white_square
		if board[row+1][col] == white_square:
			board[row+1][col] = black_square
		elif board[row+1][col] == black_square:
			board[row+1][col] = white_square
		if board[row-1][col] == white_square:
			board[row-1][col] = black_square
		elif board[row-1][col] == black_square
			board[row-1][col] = white_square

	elif board[row][col] == black_square:
		board[row][col] = white_square
		if board[row][col+1] == white_square:
			board[row][col+1] = black_square
		elif board[row][col+1] == black_square:
			board[row][col+1] = white_square
		if board[row][col-1] == white_square:
			board[row][col-1] = black_square
		elif board[row][col-1] == black_square:
			board[row][col-1] = white_square
		if board[row+1][col] == white_square:
			board[row+1][col] = black_square
		elif board[row+1][col] == black_square:
			board[row+1][col] = white_square
		if board[row-1][col] == white_square:
			board[row-1][col] = black_square
		elif board[row-1][col] == black_square
			board[row-1][col] = white_square

	


#def is_solved():


main()
