# Create a Tic-Tac-Toe game in Python by utilizing prompt engineering concepts to generate a series of prompts that will allow you to accomplish this task.

# FEATURES

# User input:
# - User inputs their move for each turn:
# - Maybe we do this by user inputting row and column for their move.
# - Ask the user if they want to be 'x' or 'o'
# Show the board with the current state of the game 
# -Check after every move to see if :
#    -someone won
#    -Cats game

#  GAME FLOW
# - Who goes first? Player A
# - Player A makes their move
# - Now it's player B's Turn, and play B makes their move
#  .... and so on ...

# - Need to be able to see the board
# - Prompt for their move
# -We need tell the user how to enter their move

# COMPUTER PLAYER
# - Needs to know if spots available or if there is an available spot or not 

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return (move - 1) // 3, (move - 1) % 3
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_symbol = 'X'
    computer_symbol = 'O'

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)

        # Player's turn
        player_row, player_col = get_player_move()
        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = player_symbol
        else:
            print("Invalid move. That cell is already taken. Try again.")
            continue

        if check_winner(board, player_symbol):
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer's turn
        print("Computer's turn...")
        computer_row, computer_col = get_computer_move(board)
        board[computer_row][computer_col] = computer_symbol

        if check_winner(board, computer_symbol):
            print_board(board)
            print("Sorry, the computer wins. Try again.")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()