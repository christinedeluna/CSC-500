#!/usr/bin/python

def main():
    # Ask the user for the number of books purchased
    books_purchased = int(input("Enter the number of books purchased this month: "))
    
    # Determine the number of points earned
    if books_purchased >= 0 and books_purchased < 2:
        points = 0
    elif books_purchased >= 2 and books_purchased < 4:
        points = 5
    elif books_purchased >= 4 and books_purchased < 6:
        points = 15
    elif books_purchased >= 6 and books_purchased < 8:
        points = 30
    elif books_purchased >= 8:
        points = 60
    else:
        points = 0  # Default case for numbers that don't match the criteria
    
    # Display the points earned
    print(f"You have earned {points} points.")
    
# Run the program
if __name__ == "__main__":
    main()
