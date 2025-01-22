#!/usr/bin/python

def divide_numbers(a: float, b: float) -> float:
    """Divides two numbers and returns the result.
    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of division.

    Raises:
        ValueError: If b is zero, raises an exception to avoid division by zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

# Example usage of divide_numbers function
if __name__ == "__main__":
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        print("Result:", divide_numbers(num1, num2))
    except ValueError as e:
        print("Error:", e)
