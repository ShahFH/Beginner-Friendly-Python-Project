import os

# Initialize the board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Define the print_board function
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Define the get_move function
def get_move(player):
    while True:
        move = input(player + "'s turn (X/O). Enter a cell number (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
            return int(move)
        else:
            print("Invalid move. Please try again.")

# Define the check_win function
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    # No win
    return False

# Define the main function
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Tic Tac Toe!")
    print_board()
    while True:
        # Player 1 move
        move = get_move("Player 1")
        board[move-1] = "X"
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()
        if check_win("X"):
            print("Player 1 wins!")
            break
        if " " not in board:
            print("Tie!")
            break
        # Player 2 move
        move = get_move("Player 2")
        board[move-1] = "O"
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board()
        if check_win("O"):
            print("Player 2 wins!")
            break

# Run the game
if __name__ == "__main__":
    main()
