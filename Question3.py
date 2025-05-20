# Using functions, write a program to compute the area and perimeter of a square. 
# The program should ask the user to enter a number corresponding to the side length of the square and display the area and perimeter of the square.

import math

def area_of_square(side_length):
    area = side_length ** 2
    return area

def perimeter_of_square(side_length):
    perimeter = 4 * side_length
    return perimeter

while True:
    # Prompt user to input side length
    side_length_input = input("Enter the side length of the square in cm: ").strip()

    # Ensure input is a valid float
    try:
        side_length = float(side_length_input)
        if side_length <= 0:
            print("⚠️ Please enter a positive number for the side length.\n")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number for the side length.\n")
        continue

    # Print the area and perimeter of the square    
    print(f"\n🧮 The area of the square with side length {side_length:.2f} cm is {area_of_square(side_length):,.3f} cm².")
    print(f"📏 The perimeter of the square with side length {side_length:.2f} cm is {perimeter_of_square(side_length):,.3f} cm.\n")

    # Ask if user wants to perform another calculation
    choice = input("Do you want to calculate another square? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Goodbye!")
        break
