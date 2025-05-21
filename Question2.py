# Write a program that asks a user to input the radius then the program calculates the volume of a sphere. 
# Use the exponential operator in python to compute (r³)


import math

while True:
    # Prompt user to input radius
    radius_input = input("Enter the radius of the sphere in cm: ").strip()

    # Ensure only valid float input is accepted and ensure it is positive
    try:
        radius = float(radius_input)
        if radius <= 0:
            print("Please enter a positive number for the radius.\n")
            continue
    except ValueError:
        print("Please enter a valid number for the radius.\n")
        continue

    # Calculate the volume of the sphere using the exponential operator (**)
    volume = (4 / 3) * math.pi * (radius ** 3)

    # Display the result, rounded to 3 decimal places
    print(f"\n The volume of a sphere with radius {radius:.2f} cm is {volume:,.3f} cm³.\n")

    # Ask if user wants to calculate again
    choice = input("Do you want to calculate another volume? (yes/no): ").strip().lower()
    if choice not in ['yes', 'y']:
        print("Goodbye!")
        break
