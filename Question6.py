# Write a Python program that uses a loop for a user to continually input 5 values to populate an array
# Calculates and displays the average of the values input into the array.


# Create an empty list to store the values
values = []


# Loop to get 5 values from the user
for i in range(5):
    while True:
        try:
            # Get user input
            value = float(input(f"Enter value {i + 1}: "))
            values.append(value)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Calculate the average
average = sum(values) / len(values)


# Display the average
print(f"The average of the values is: {average}")

