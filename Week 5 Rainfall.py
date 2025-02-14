def main():
    # Ask the user for the number of years
    years = int(input("Enter the number of years: "))
    
    # Initialize total rainfall and month count
    total_rainfall = 0
    total_months = years * 12  # Since each year has 12 months
    
    # Loop through each year
    for year in range(1, years + 1):
        print(f"Year {year}")
        yearly_rainfall = 0
        
        # Loop through each month
        for month in range(1, 13):
            while True:
                try:
                    rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative. Please enter a valid number.")
                        continue
                    yearly_rainfall += rainfall
                    total_rainfall += rainfall
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        
        yearly_average = yearly_rainfall / 12
        print(f"Year {year} average rainfall: {yearly_average:.2f} inches\n")
    
    # Calculate average rainfall per month
    average_rainfall = total_rainfall / total_months
    
    # Display results
    print("\nRainfall Statistics")
    print(f"Total months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
    
# Run the program
if __name__ == "__main__":
    main()
