import math
import random

SIZE = 3
HUMAN = "X"
COMP = "O"
board = None

def check_for_win(board):
  # Check for horizontal wins
  for y in range(SIZE):
    row = "".join(map(str,board[y]))
    if row == HUMAN * 3:
      return HUMAN
    elif row == COMP * 3:
      return COMP
  
  # Check for vertical wins
  for x in range(SIZE):
    column = "".join(map(str,[board[y][x] for y in range(SIZE)]))
    if column == HUMAN * 3:
      return HUMAN
    elif column == COMP * 3:
      return COMP
  
  # Check for diagonal wins
  tl_br = "".join(map(str,[board[k][k] for k in range(SIZE)]))
  if tl_br == HUMAN * 3:
    return HUMAN
  elif tl_br == COMP * 3:
    return COMP
  
  tr_bl = "".join(map(str,[board[k][SIZE-k-1] for k in range(SIZE)]))
  if tr_bl == HUMAN * 3:
    return HUMAN
  elif tr_bl == COMP * 3:
    return COMP
  
  return None

def num_to_row_and_column(num):
  num -= 1
  row = math.floor(num / SIZE)
  column = num % 3
  return row, column

def print_board(board):
  print()
  print((f"\n{'-'*11}\n").join(["|".join([f" {char} " for char in row]) for row in board]))
  print()

def is_valid_space(board, num):
  row, column = num_to_row_and_column(num)
  return isinstance(board[row][column], int)

def set_space(board, num, player):
  row, column = num_to_row_and_column(num)
  board[row][column] = player

def tictactoe():
  global board
  board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
  player = HUMAN
  while (winner := check_for_win(board)) is None:
    print_board(board)
    available_places = [board[row][column] for row in range(SIZE) for column in range(SIZE) if is_valid_space(board, 3*row + column + 1)]
    if len(available_places) == 0:
      winner = "Tie"
      break
    if player == HUMAN:
      print("What position would you like to play in?")
      while not (valid_position := False):
        try:
          response = int(input())
        except ValueError:
          print("Invalid input, please try again.")
          continue
        if response in range(1, 9 + 1) and is_valid_space(board, response):
          set_space(board, response, player)
          break
        print("Invalid input, please try again.")
    elif player == COMP:
      place = random.choice(available_places)
      print(f"I'm going to play at spot number {place}.")
      set_space(board, place, COMP)
    player = COMP if player == HUMAN else HUMAN
  
  print_board(board)

  if winner == HUMAN:
    print(f"Congratulations... you win.")
  elif winner == COMP:
    print(f"Yay! I won :D Good game.")
  else:
    print(f"This game resulted in a tie.")

if __name__ == "__main__":
  tictactoe()