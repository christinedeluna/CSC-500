import re  # Import regular expressions for better input handling

def get_valid_hour():
    while True:
        user_input = input("Enter the current time (0-23 in 24-hour format, e.g., 0 for Midnight, 13 for 1PM, 23 for 11PM): ").strip()

        # Extract numbers using regex, allowing for formats like "08:00" or "8:00"
        match = re.match(r"(\d+)", user_input)
        if match:
            current_time = int(match.group(1))  # Extract the first number

            if 0 <= current_time <= 23:
                return current_time  # Return valid hour
            else:
                print("Invalid input! Please enter a number between 0 and 23.")
        else:
            print("Invalid format! Enter only the hour as a number (e.g., 8, 13, 23).")

def get_valid_wait_time():
    while True:
        try:
            hours_to_wait = int(input("Enter the number of hours to wait for the alarm: ").strip())

            if hours_to_wait >= 0:
                return hours_to_wait  # Return valid hours to wait
            else:
                print("Invalid input! Please enter a non-negative number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_alarm_time():
    current_time = get_valid_hour()
    hours_to_wait = get_valid_wait_time()

    # Calculate the alarm time
    alarm_time = (current_time + hours_to_wait) % 24

    # Display the result
    print(f"\nThe alarm will go off at {alarm_time}:00 (24-hour format).")

# Run the function
calculate_alarm_time()



