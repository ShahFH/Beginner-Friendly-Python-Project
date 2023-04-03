def is_palindrome(input):
    """
    Checks if the input is a palindrome. Returns True if it is, False otherwise.
    """
    input_str = str(input)
    return input_str == input_str[::-1]

def palindrome_checker():
    """
    Prompts the user to enter a string, number, or list to check for palindromes.
    """
    input_type = input("What type of input would you like to check? (string, number, list): ")
    input_value = input("Enter the input value: ")

    if input_type == "string":
        if is_palindrome(input_value):
            print(f"{input_value} is a palindrome!")
        else:
            print(f"{input_value} is not a palindrome.")

    elif input_type == "number":
        if is_palindrome(input_value):
            print(f"{input_value} is a palindrome!")
        else:
            print(f"{input_value} is not a palindrome.")

    elif input_type == "list":
        if is_palindrome(input_value):
            print(f"{input_value} is a palindrome!")
        else:
            print(f"{input_value} is not a palindrome.")
