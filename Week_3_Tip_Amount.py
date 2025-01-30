#!/usr/bin/python

def calculate_total_meal_cost():
    # Constants for tip and tax rates
    TIP_RATE = 0.18
    TAX_RATE = 0.07
    
    # Get the meal charge from the user
    meal_cost = float(input("Enter the charge for the food: "))
    
    # Calculate tip and tax amounts
    tip_amount = meal_cost * TIP_RATE
    tax_amount = meal_cost * TAX_RATE
    
    # Calculate total cost
    total_cost = meal_cost + tip_amount + tax_amount
    
    # Display the results
    print(f"\nMeal Cost: ${meal_cost:.2f}")
    print(f"Tip (18%): ${tip_amount:.2f}")
    print(f"Sales Tax (7%): ${tax_amount:.2f}")
    print(f"Total Amount: ${total_cost:.2f}")

# Run the function
calculate_total_meal_cost()

