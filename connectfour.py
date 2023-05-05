import random
import sys
import time
board = [[" " for _ in range(7)] for _ in range(6)]

def draw_board(board):
    print("1 2 3 4 5 6 7")
    for row in board:
        print("|".join(str(cell) for cell in row))
draw_board(board)

def player_move(board):
    while True:
        try:
            user_choice = int(input('Where do you want to go? 1, 2, 3, 4, 5, 6 or 7?: '))
            if not (0<= user_choice < 7):
                print("Invalid number. Please enter a number between 1 and 7: ")
            else:
                for row in range(5, -1, -1):
                    if board[row][user_choice-1] == " ":
                        board[row][user_choice-1] = 'X'
                        draw_board(board)
                        return
                print("That column is already full. Please choose another column: ")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7: ")
def computer_move(board):
    while True:
        computer_choice = (random.randint(0, 6))
        for row in range(5, -1, -1):
            if board[row][int(computer_choice)] == ' ':
                board[row][int(computer_choice)] = 'O'
                draw_board(board)
                (time.sleep(0.6))
                print('The computer chose '+ str(computer_choice + 1))
                return
def check_win(board):
    for row in board:
        for i in range(len(row) - 3):
            if row[i] != ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                return True
    for i in range(len(board[0])):
        for j in range(len(board) - 3):
            if board[j][i] != ' ' and board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i]:
                return True
    for i in range(len(board[0]) - 3):
        for j in range(len(board) - 3):
            if board[j][i] != ' ' and board[j][i] == board[j+1][i+1] == board[j+2][i+2] == board[j+3][i+3]:
                return True
            if board[j][i+3] != ' ' and board[j][i+3] == board[j+1][i+2] == board[j+2][i+1] == board[j+3][i]:
                return True
    return False
while True:    
    player_move(board)
    time.sleep(1)
    computer_move(board)
    check_win(board)
    if check_win(board) == True:
        print("Game over! a player has won")
        sys.exit()
