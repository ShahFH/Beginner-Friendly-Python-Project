import random

# Open the file containing the jokes
with open('jokes.txt', 'r') as file:
    jokes = file.readlines()

# Select a random joke from the list
joke = random.choice(jokes)

# Print the joke to the console
print(joke)
