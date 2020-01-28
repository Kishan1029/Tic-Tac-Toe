#-------------GLOBAL Variable--------------#

#game board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

#If game is still game still going 
game_still_going = True

#Who won or Tie
Winner = None

#whos turn
current_player = "X"
 
def display_board():
  print(board[0]+ "|" + board[1] + "|" + board[2])
  print(board[3]+ "|" + board[4] + "|" + board[5])
  print(board[6]+ "|" + board[7] + "|" + board[8])

def play_game():
  #display empty board
  display_board()
  while game_still_going:

    #handle a single turn of arbitrary player
    handle_turn(current_player)


    #check if game is over
    check_if_game_over()

    #Rotate the player
    flip_player()

  #The game has ended
  if Winner == "X" or Winner == "O":
    print(Winner + " won")
  elif Winner == None:
    print("Tie. ")

#handle a single turn of arbitrary player
def handle_turn(player):

  print(player + "s turn.")
  position = input("Choose a position from 1-9: ")
  
  vaild = False
  while not vaild:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invaild input. Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position]  == "-":
      vaild = True
    else:
      print("You cant go there. Go Agian.")
  
  board[position] = player
  display_board()


def check_if_game_over():
  check_winner()
  check_draw()


def check_winner():

  #to set the global variable
  global Winner

  #check rows, columns, diagonals
  row = check_rows()

  column = check_column()
  
  diagonal = check_diagonals()

  if row:
    #there is winner
    Winner = check_rows()
  elif column:
    #there is winner
    Winner = check_column()
  elif diagonal:
    #winner diagonaly
    Winner = check_diagonals()
  else: 
    #there was no win
    Winner = None
  return

def check_rows():

  #set global variable 
  global game_still_going

  #check if any of rows matches
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  #if any rows has match mark the win
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[2]
  elif row_3:
    return board[6]

  return


def check_column():
    #set global variable 
  global game_still_going

  #check if any of rows matches
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  
  #if any rows has match mark the win
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagonals():
  global game_still_going

  #check if any of rows matches
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  #if any rows has match mark the win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  return


def check_draw():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  #chaning the current player
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

play_game()
