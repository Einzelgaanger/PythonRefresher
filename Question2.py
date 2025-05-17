# Write a program that asks a user to input the radius then the program calculates the volume of a sphere. 
# Use the exponential operator in python to compute (r³)


# Prompt user to input radius
radius = input("Enter the radius of the circle: ")


# Ensure only float input is accepted and ensure it is positive
try:
    radius = float(radius)
    if radius <= 0:
        print("Please enter a positive number for the radius.")
        exit()
except ValueError:
    print("Please enter a valid number for the radius.")
    exit()


# Calculate the volume of the sphere
import math 

volume = (4/3) * math.pi * radius**3


# Display the result
print(f"The volume of the sphere with radius {radius} cm is {volume:.3f} cm³.")
