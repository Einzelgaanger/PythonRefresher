# Define a function to check if the character is uppercase or lowercase
def check_case(char):
    if len(char) != 1:
        return "is not a single character"
    elif not char.isalpha():
        return "not an alphabetic character"
    elif char.isupper():
        return "uppercase"
    elif char.islower():
        return "lowercase"
    else:
        return "Try again"

while True:
    # Prompt the user for a character
    char = input("Enter a character (e.g., k, L): ").strip()

    # Print the result
    print(f"The character '{char}' is {check_case(char)}.\n")

    # Ask if the user wants to continue
    choice = input("Do you want to check another character? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Goodbye!")
        break
