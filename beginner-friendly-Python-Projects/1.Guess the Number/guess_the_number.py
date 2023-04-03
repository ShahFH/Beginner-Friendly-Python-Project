import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Keep track of the number of guesses
num_guesses = 0

while True:
    guess = int(input("Enter your guess: "))
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print(f"Congratulations, you guessed the number in {num_guesses} guesses!")
        break
    
    # Provide feedback on the guess
    elif guess < number:
        print("Too low! Guess again.")
    
    else:
        print("Too high! Guess again.")
