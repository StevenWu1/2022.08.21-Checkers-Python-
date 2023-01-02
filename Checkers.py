pieces = [
    [0, 2, 0, 2, 0, 2, 0, 2], 
    [2, 0, 2, 0, 2, 0, 2, 0], 
    [0, 2, 0, 2, 0, 2, 0, 2], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 2, 0, 0, 0, 0, 0, 0], 
    [1, 0, 1, 0, 1, 0, 1, 0], 
    [0, 1, 0, 1, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 0, 1, 0]]

def check_king():
  for i in range(8):
    if pieces[0][i] == 1:
      pieces[0][i] = 3
    if pieces[7][i] == 2:
      pieces[0][i] = 4

def valid_move(player, pos_row, pos_col, pos_rowm, pos_colm):
  #check if selected position is valid
  opposing = 0
  if player == 1:
    opposing = 2
  else:
    opposing = 1
  if pieces[pos_row][pos_col] == player:
    if pieces[pos_rowm][pos_colm] != player and pieces[pos_rowm][pos_colm] != opposing:
      #check if move position is valid
      valid_row = pos_row - pos_rowm
      valid_col = pos_col - pos_colm
      if valid_row == 1 or valid_row == -1:
        if valid_col == 1 or valid_col == -1:
          pieces[pos_row][pos_col] = 0
          pieces[pos_rowm][pos_colm] = player
          check_king()
          update_board(pieces)

def valid_eat(player, pos_row, pos_col, pos_rowm, pos_colm):
  opposing = 0
  if player == 1:
    opposing = 2
  else:
    opposing = 1
  valid_row = int(pos_row - pos_rowm)
  valid_col = int(pos_col - pos_colm)
  eaten_row = int((pos_row + pos_rowm) / 2)
  eaten_col = int((pos_col + pos_colm) / 2)
  if pieces[pos_row][pos_col] == player:
    if pieces[int(eaten_row)][int(eaten_col)] == opposing or pieces[int(eaten_row)][int(eaten_col)] == opposing + 2:
      if valid_row == 2 or valid_row == -2:
        if valid_col == 2 or valid_col == (-2):
          if pieces[pos_rowm][pos_colm] != 1 and pieces[pos_rowm][pos_colm] != 2:
            pieces[pos_row][pos_col] = 0
            pieces[int(eaten_row)][int(eaten_col)] = 0
            pieces[pos_rowm][pos_colm] = player
            print("")
            check_king()
            update_board(pieces)

def valid_king_move(player, pos_row, pos_col, pos_rowm, pos_colm):
  #check if selected position is valid
  opposing = 0
  if player == 1:
    opposing = 2
  else:
    opposing = 1
  if pieces[pos_row][pos_col] == player + 2:
    if pieces[pos_rowm][pos_colm] != player and pieces[pos_rowm][pos_colm] != opposing:
      #check if move position is valid
      valid_row = pos_row - pos_rowm
      valid_col = pos_col - pos_colm
      if valid_row == 1 or valid_row == -1:
        if valid_col == 1 or valid_col == -1:
          pieces[pos_row][pos_col] = 0
          pieces[pos_rowm][pos_colm] = player + 2
          check_king()
          update_board(pieces)

def valid_king_eat(player, pos_row, pos_col, pos_rowm, pos_colm):
  opposing = 0
  if player == 1:
    opposing = 2
  else:
    opposing = 1
  valid_row = int(pos_row - pos_rowm)
  valid_col = int(pos_col - pos_colm)
  eaten_row = int((pos_row + pos_rowm) / 2)
  eaten_col = int((pos_col + pos_colm) / 2)
  if pieces[pos_row][pos_col] == player + 2:
    if pieces[int(eaten_row)][int(eaten_col)] == opposing or pieces[int(eaten_row)][int(eaten_col)] == opposing + 2:
      if valid_row == 2 or valid_row == -2:
        if valid_col == 2 or valid_col == -2:
          if pieces[pos_rowm][pos_colm] != 1 and pieces[pos_rowm][pos_colm] != 2:
            pieces[pos_row][pos_col] = 0
            pieces[int(eaten_row)][int(eaten_col)] = 0
            pieces[pos_rowm][pos_colm] = player + 2
            print("")
            check_king()
            update_board(pieces)

def update_board(pieces):
	newboard = []
	for list in pieces:
		for i in list:
			if i == 0:
				newboard.append(".") #blank
			if i == 1:
				newboard.append("x") #Normal 1
			if i == 2:
				newboard.append("o") #Normal 2
			if i == 3:
				newboard.append("X") #King 1
			if i == 4:
				newboard.append("O") #King 2
        
	newboard = " ".join(newboard)
	print("  0 1 2 3 4 5 6 7")
	print("0 " + newboard[:16])
	print("1 " + newboard[16:32])
	print("2 " + newboard[32:48])
	print("3 " + newboard[48:64])
	print("4 " + newboard[64:80])
	print("5 " + newboard[80:96])
	print("6 " + newboard[96:112])
	print("7 " + newboard[112:128])

board_setup = ("""
  0 1 2 3 4 5 6 7
0 . o . o . o . o 
1 o . o . o . o . 
2 . o . o . o . o 
3 . . . . . . . . 
4 . . . . . . . . 
5 x . x . x . x . 
6 . x . x . x . x 
7 x . x . x . x .
""")



start = input("Would you like to play checkers? (Y/N) ")
while start == "Y":
  check_king()
  update_board(pieces)
  while start == "Y":
    #player 1
    player = 1
    print("PLAYER", player)
    row = int(input("Which row would you like to select? "))
    col = int(input("Which column would you like to select? "))
    rowm = int(input("Which row would you like to move to? "))
    colm = int(input("Which column would you like to move to? "))
    
    valid_row = row - rowm
    valid_col = col - colm
    if pieces[row][col] == 3:
      if valid_row == -1 or valid_row == 1:
        if valid_col == 1 or valid_col == -1:
          valid_king_move(player, row, col, rowm, colm)
          print("Player 1 moved piece", row, col, "to", rowm, colm)
      else:
        valid_king_eat(player, row, col, rowm, colm)
        print("Player 1 moved piece", row, col, "to", rowm, colm)
        print("Player 1 eats one piece")
    if pieces[row][col] == 1:
      if valid_row == 1:
        if valid_col == 1 or valid_col == -1:
          valid_move(player, row, col, rowm, colm)
          print("Player 1 moved piece", row, col, "to", rowm, colm)
      else:
          valid_eat(player, row, col, rowm, colm)
          print("Player 1 moved piece", row, col, "to", rowm, colm)
          print("Player 1 eats one piece")
    # check if game is still running
    if str(2) not in str(pieces):
      if str(4) not in str(pieces):
        print("Player 1 WINS")
        start = "N"
    
    #player 2
    player = 2
    print("PLAYER", player)
    row = int(input("Which row would you like to select? "))
    col = int(input("Which column would you like to select? "))
    rowm = int(input("Which row would you like to move to? "))
    colm = int(input("Which column would you like to move to? "))
    
    valid_row = row - rowm
    valid_col = col - colm
    if pieces[row][col] == 4:
        if valid_row == -1 or valid_row == 1:
          if valid_col == 1 or valid_col == -1:
            valid_king_move(player, row, col, rowm, colm)
            print("Player 2 moved piece", row, col, "to", rowm, colm)
        else:
          valid_king_eat(player, row, col, rowm, colm)
          print("Player 1 moved piece", row, col, "to", rowm, colm)
          print("Player 1 eats one piece")
    if pieces[row][col] == 2:
      if valid_row == -1:
        if valid_col == 1 or valid_col == -1:
          valid_move(player, row, col, rowm, colm)
          print("Player 2 moved piece", row, col, "to", rowm, colm)
      else:
        valid_eat(player, row, col, rowm, colm)
        print("Player 2 moved piece", row, col, "to", rowm, colm)
        print("Player 2 eats one piece")
    # Check if game has ended
    if str(1) not in str(pieces):
      if str(3) not in str(pieces):
        print("PLAYER 2 WINS")
        start = "N"
