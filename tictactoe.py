import random
import time

def who_goes_first():
    possible_coin_choices = ["heads", "tails"]
    heads_or_tails = random.choice(possible_coin_choices)
    print("Welcome to tic tac toe, let's see who goes first.")
    while True:
        user_coin_choice = input("Choose heads or tails: ").lower()
        if user_coin_choice in possible_coin_choices:
            if user_coin_choice == heads_or_tails:
                print("Urgh, you go first.")
                return "X"
            else:
                print("Lol, I go first!")
                return "O"
        else: print("Bro...")
time.sleep(1)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

board = [[" " for _ in range(3)] for _ in range(3)] 

def user_choice(board):
    while True:
        try:
            choice = int(input("Choose a position from 1-9: "))
            if choice < 1 or choice > 9:
                print("Bro are you dumb, c'mon: ")
                continue
            
            row = (choice - 1) // 3
            col = (choice - 1) % 3
            
            if board[row][col] != " ":
                print("Go to Specsavers, that position is taken.")
            else:
                board[row][col] = "X"  
                break
        except ValueError:
            print("Oh my gawd, bru, enter a number between 1 and 9 inclusive.")

def computer_choice(board):
    available_positions = [i for i in range(1, 10) if board[(i-1)//3][(i-1)%3] == " "]
    if available_positions:
        choice = random.choice(available_positions)
        row = (choice - 1) // 3
        col = (choice - 1) % 3
        board[row][col] = "O"  
        print(f"I chose position {choice}.")

def check_winner(board):
  
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]  
  
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]  
   
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2] 
    return None  

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    current_player = who_goes_first()
    game_over = False
    while not game_over:
        print_board(board)
        if current_player == "X":
            user_choice(board)
        else:
            computer_choice(board)

        winner = check_winner(board)
        if winner: 
            print_board(board) 
            if winner == "X":
                print("Damn :/ you won")
            else:
                print("HAHA I WON")
            break 
        
        if check_draw(board): 
            print_board(board)
            print("How do you draw with a computer?")
            break 
        
        current_player = "O" if current_player == "X" else "X" 

    print("Game over!")

tic_tac_toe()
