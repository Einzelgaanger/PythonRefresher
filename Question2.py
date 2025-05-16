# Write a program that asks a user to input the radius then the program calculates the volume of a sphere. Use the exponential operator in python to compute (r³)
# Prompt user to input radius
radius = input("Enter the radius of the circle: ")


# Ensure only float input is accepted
try:
    is_float = float(radius)
    float_input = True
except ValueError:
    float_input = False

if not float_input:
    print("Please enter a valid float.")
    exit()


# Ensure only positive float input is accepted
try:
    no_radius = 0
    then_radius = True
except ValueError:
    then_radius = False

if then_radius:
    print("Please enter a valid positive number of radius.")
    exit()


# Calculate the volume of the sphere
import math 
volume = float((4/3) * math.pi * radius**3)
print(f"The volume of the sphere with radius {radius}cm is {volume:.3f}cm³.") 