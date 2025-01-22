#!/usr/bin/python

# addition_solution.py
def add_numbers():
    try:
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the sum
        result = num1 + num2

        # Display the result
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the function
if __name__ == "__main__":
    add_numbers()
