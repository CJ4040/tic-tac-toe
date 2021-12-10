from IPython.display import clear_output
import random

def display_board(board) :
    clear_output()
    print("    |   |    ")
    print("  " + board[1] + " | " + board[2] + " | " + board[3])
    print("____|___|____")
    print("    |   |    ")
    print("  " + board[4] + " | " + board[5] + " | " + board[6])
    print("____|___|____")
    print("    |   |    ")
    print("  " + board[7] + " | " + board[8] + " | " + board[9])
    print("    |   |    ")

def player_input() :
    
    #Initial set to blank
    choice = "nothing"
    
    #continue asking if player choice is not X or O.
    while choice not in ["X","O"] :
    
        choice = input('Please choose your marker (X or O): ').upper()
        
        if choice == "X" : 
            return ("X","O")
        
        elif choice == "O":
            return ("O","X")
        
        else :
            print("I don't understand, please enter X or O : ")

def choose_first():
    return f"Player {random.randint(1,2)}"
        
def player_choice(board) :
    
    position = 0
    
    while position not in range (1,len(board)+1) or not space_check(board, position):
        
        position = int(input("Please enter a number from 1-9: "))
        
    return position      
            
    
def place_marker(board, marker, position):
    
    board[position] = marker

    
def check_win(board,marker): 
  
    win = False
    
    diagonals = [board[1:10:4],board[3:8:2]]
    columns = [board[1:8:3],board[2:9:3],board[3:10:3]]
    rows = [board[1:4],board[4:7],board[7::]]
    
    for x in columns :
        if len(set(x)) == 1 and x[0] == marker : #convert each column to a set. If its length is 1 AND the first element in the set = marker, its a win
            win = True
    for x in rows :
        if len(set(x)) == 1 and x[0] == marker : #convert each row to a set. If its length 1, someone has won.
            win = True
    for x in diagonals :
        if len(set(x)) == 1 and x[0] == marker : #convert each diagonal to a set. If its length 1, someone has won.
            win = True
        
    return win
  
def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    
    for i in range(1,len(board)) :
        
        if space_check(board, i):
            return False
    return True


def replay() :
        
    answer = input("Do you want to play again (y or n): ")
        
    return bool(answer == "y")


while True : #set up the game
    board = [' '] *10
    begin_game = input("Welcome to tic, tac, toe!\nAre you ready to play? (y / n): ")
    
    if begin_game[0] == "y" :
        player1_marker, player2_marker = player_input() #assign a marker to each player
        turn = choose_first() # choose who goes first
        print(f"\nPlayer 1 will be {player1_marker}, Player 2 will be {player2_marker} ")
        print(f"{turn} will go first")
        game_on = True
        
    else :
        game_on = False
        break
        
    while game_on :
            
        if turn == "Player 1":
            position = player_choice(board) # player chooses a position on the board
            place_marker(board, player1_marker, position) # marker is placed on the board
            display_board(board)
            
            if check_win(board,player1_marker) == True:
                print(f"{turn} has won the game!")
                game_on = False #end the game as the player has won
            
            else :
                if full_board_check(board) == True :
                    print("its a draw!")
                    break
                turn = "Player 2"
        
        else : # its player 2's turn
            position = player_choice(board) # player chooses a position on the board
            place_marker(board, player2_marker, position) # marker is placed on the board
            display_board(board)
            
            if check_win(board,player2_marker) == True:
                print(f"{turn} has won the game!")
                game_on = False #end the game as the player has won
            
            else :
                if full_board_check(board) == True :
                    print("its a draw!")
                    break
                turn = "Player 1"
                
    if not replay():
        break
