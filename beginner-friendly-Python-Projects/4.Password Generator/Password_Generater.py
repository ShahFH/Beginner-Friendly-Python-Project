import string
import random

# Define the Password Generator Function
def generate_password(length):
    # Define the characters to use in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine the characters into a single string
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Use random.choices() to generate the password
    password = ''.join(random.choices(all_characters, k=length))
    return password

# Get Input from User
length = int(input("Enter the length of the password: "))

# Generate the Password and Print
password = generate_password(length)
print("Your new password is:", password)
