 #Kendra Ludwig (kel334@nau.edu)
 #Michael Reed (msr248@nau.edu)


import random


def main():
    white_square = "\N{WHITE SQUARE}"
    black_square = "\N{BLACK SQUARE}"
    squares = [white_square, black_square]
    moves = 0

    board = [[random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)],
            [random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares), random.choice(squares)]]

    for row in board:
        board = row[0], row[1], row[2], row[3], row[4]
        print(row[0], row[1], row[2], row[3], row[4])
	
    x = int(input("Please pick a row number between 0 and 4: "))
    y = int(input("Please pick a column number between 0 and 4: "))
    row = x
    col = y

    moves = 0
    while white_square != 0:
        (row, col) = ask_row_and_col()
        touch(board, row, col)
        moves += 1
    print(row[0], row[1], row[2], row[3], row[4])
    print(f"You won with {moves} moves!")


def ask_row_and_col():
    x = int(input("Please pick a row number between 0 and 4: "))
    y = int(input("Please pick a column number between 0 and 4: "))

    if x > 4 or x < 0:
        x = int(input("Please pick a row number between 0 and 4: "))


    if y > 4 or y < 0:
        y = int(input("Please pick a column number between 0 and 4: "))

#change swap the colors of the touching squares
#includes: one up, one down, one left, one right
def touch(board, row, col):
	for i in range(1, 4):
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
			elif board[row-1][col] == black_square:
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
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

	#accounts for edges and corners wrapping 
	if row == 0:
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

	if row == 4:
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
			if board[row-1][col] == white_square:
				board[row-1][col] = white_square
			elif board[row-1][col] == black_square:
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
			if board[row-1][col] == white_square:
				board[row-1][col] = black_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

	if col == 0:
		if board[row][col] == white_square:
			board[row][col] = black_square
			if board[row][col+1] == white_square:
				board[row][col+1] = black_square
			elif board[row][col+1] == black_square:
				board[row][col+1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = white_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

		elif board[row][col] == black_square:
			board[row][col] = white_square
			if board[row][col+1] == white_square:
				board[row][col+1] = black_square
			elif board[row][col+1] == black_square:
				board[row][col+1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = black_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

	if col == 4:
		if board[row][col] == white_square:
			board[row][col] = black_square
			if board[row][col-1] == white_square:
				board[row][col-1] = black_square
			elif board[row][col-1] == black_square:
				board[row][col-1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = white_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

		elif board[row][col] == black_square:
			board[row][col] = white_square
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
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

	if row == 0 and col == 0:
		if board[row][col] == white_square:
			board[row][col] = black_square
			if board[row][col+1] == white_square:
				board[row][col+1] = black_square
			elif board[row][col+1] == black_square:
				board[row][col+1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square

		elif board[row][col] == black_square:
			board[row][col] = white_square
			if board[row][col+1] == white_square:
				board[row][col+1] = black_square
			elif board[row][col+1] == black_square:
				board[row][col+1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square
	
	if row == 0 and col == 4:
		if board[row][col] == white_square:
			board[row][col] = black_square
			if board[row][col+1] == white_square:
				board[row][col+1] = black_square
			elif board[row][col+1] == black_square:
				board[row][col+1] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = black_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

		elif board[row][col] == black_square:
			board[row][col] = white_square
			if board[row][col+1] == white_square:
				board[row][col+1] = black_square
			elif board[row][col+1] == black_square:
				board[row][col+1] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = black_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square
	
	if row == 4 and col == 0:
		if board[row][col] == white_square:
			board[row][col] = black_square
			if board[row][col-1] == white_square:
				board[row][col-1] = black_square
			elif board[row][col-1] == black_square:
				board[row][col-1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square

		elif board[row][col] == black_square:
			board[row][col] = white_square
			if board[row][col-1] == white_square:
				board[row][col-1] = black_square
			elif board[row][col-1] == black_square:
				board[row][col-1] = white_square
			if board[row+1][col] == white_square:
				board[row+1][col] = black_square
			elif board[row+1][col] == black_square:
				board[row+1][col] = white_square
	
	if row == 4 and col == 4:
		if board[row][col] == white_square:
			board[row][col] = black_square
			if board[row][col-1] == white_square:
				board[row][col-1] = black_square
			elif board[row][col-1] == black_square:
				board[row][col-1] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = black_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square

		elif board[row][col] == black_square:
			board[row][col] = white_square
			if board[row][col-1] == white_square:
				board[row][col-1] = black_square
			elif board[row][col-1] == black_square:
				board[row][col-1] = white_square
			if board[row-1][col] == white_square:
				board[row-1][col] = black_square
			elif board[row-1][col] == black_square:
				board[row-1][col] = white_square


main()
