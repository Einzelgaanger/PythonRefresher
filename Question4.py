# Write a program using functions that determines whether a character input by a user is uppercase or lower case.
# Prompt the user for a character
char = input("Enter a character (eg: k, L): ")


# Define a function to check if the character is uppercase or lowercase
def check_case(char):
    if char.isupper():
        return "uppercase"
    elif char.islower():
        return "lowercase"
    else:
        return "Not an alphabetic character"


# Print the result
print(f"The character '{char}' is {check_case(char)}.")
