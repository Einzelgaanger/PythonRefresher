# Write a program that asks the user for a number of days. The program then prints out the number of seconds in the number of days given.


while True:
    # Prompt user to input days

    days_input = input("Enter the number of days: ")

    # Ensure only integer input is accepted and ensure it is positive
    try:
        days = int(days_input)
        if days <= 0:
            print("Please enter a positive number of days.")
            continue
    except ValueError:
        print("Please enter a valid number of days.")
        continue

    # Calculate the number of seconds in the given number of days
    seconds = days * 24 * 60 * 60

    # Format seconds with commas if necessary
    seconds_formatted = f"{seconds:,}"

    # Output the result
    if days == 1:
        print(f"\n{days} day has {seconds_formatted} seconds.\n")
    else:
        print(f"\n{days} days have {seconds_formatted} seconds.\n")

    # Ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if choice not in ["yes", "y"]:
        print("Goodbye!")
        break
