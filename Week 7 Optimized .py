#!/usr/bin/python

# Define a single dictionary containing course information
course_info = {
    "CSC101": {"room": 3004, "instructor": "Haynes", "time": "8:00am"},
    "CSC102": {"room": 4501, "instructor": "Alvarado", "time": "9:00am"},
    "CSC103": {"room": 6755, "instructor": "Rich", "time": "10:00am"},
    "NET110": {"room": 1244, "instructor": "Burke", "time": "11:00am"},
    "COM241": {"room": 1411, "instructor": "Lee", "time": "1:00pm"}
}

# Example usage
if __name__ == "__main__":
    while True:
        course = input("Enter the course number: ").strip().upper()
        if course in course_info:
            info = course_info[course]
            print(f"The room number for {course} is: {info['room']}")
            print(f"The instructor for {course} is: {info['instructor']}")
            print(f"The meeting time for {course} is: {info['time']}")
            break
        else:
            print("Not Found, Try Again")
