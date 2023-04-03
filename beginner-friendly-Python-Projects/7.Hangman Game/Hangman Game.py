import random

# List of words for the game
words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "giraffe", "horse", "ice cream", "jellyfish", "kangaroo", "lemon", "monkey", "narwhal", "orange", "pizza", "queen", "rainbow", "strawberry", "turtle", "unicorn", "volcano", "watermelon", "xylophone", "yellow", "zebra"]

# ASCII art for the hangman
hangman = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |
    |
    |
   _|___
  |     |
  |_____|
""",
    """
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    |
    |
   _|___
  |     |
  |_____|
""",
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    |
    |
   _|___
  |     |
  |_____|
""",
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      /
    |
    |
    |
   _|___
  |     |
  |_____|
""",
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |      / \\
    |
    |
    |
   _|___
  |     |
  |_____|
"""]

# Function to choose a random word
def choose_word(difficulty):
    if difficulty == "easy":
        word = random.choice([word for word in words if len(word) <= 5])
    elif difficulty == "medium":
        word = random.choice([word for word in words if len(word) > 5 and len(word) <= 8])
    elif difficulty == "hard":
        word = random.choice([word for word in words if len(word) > 8])
    return word

# Function to play the game
def play_game():
    # Choose a difficulty level
    difficulty = input("Choose a difficulty level (easy, medium, hard): ")
    word = choose_word(difficulty)
    print(f"The word has {len(word)} letters.")

    # Initialize the game
    incorrect_guesses = 0
    correct_guesses = set()
    letters_left = set(word)

    # Play the game
    while incorrect_guesses < len(hangman) - 1 and letters_left:
        guess = input("Guess a letter: ")
        if guess in correct_guesses or guess in letters_left:
            print("You already guessed that letter!")
        elif guess in word:
            correct_guesses.add(guess)
            letters_left.remove(guess)
            print("Correct!")
        else:
            incorrect_guesses += 1
            print("Incorrect!")
        print(hangman[incorrect_guesses])
        print(" ".join([letter if letter in correct_guesses else "_" for letter in word]))
        print(f"Incorrect guesses left: {len(hangman) - 1 - incorrect_guesses}")

    # End the game
    if letters_left:
        print(f"Sorry, you ran out of guesses. The word was {word}.")
    else:
        print("Congratulations, you guessed the word!")

    # Play again?
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play_game()
    else:
       return exit
