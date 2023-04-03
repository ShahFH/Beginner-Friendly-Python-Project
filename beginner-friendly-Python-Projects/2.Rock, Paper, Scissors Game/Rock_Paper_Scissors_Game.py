import random

def play_game():
    # get user's choice
    user_choice = input("Enter Rock, Paper, or Scissors: ")

    # generate computer's choice
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    # compare the choices and determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "Paper":
        if computer_choice == "Scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid input. Please try again.");

# We'll call the play_game() function to start the game. 
# We can use a loop to allow the user to play the game multiple times if they wish.
while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
