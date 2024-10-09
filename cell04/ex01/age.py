#!/usr/bin/env python3

# Main program
if __name__ == "__main__":
    try:
        # Ask the user to enter their age
        age = int(input("Please tell me your age: "))
        
        # Display the user's current age and age in 10, 20, and 30 years
        print(f"You are currently {age} years old.")
        print(f"In 10 years, you'll be {age + 10} years old.")
        print(f"In 20 years, you'll be {age + 20} years old.")
        print(f"In 30 years, you'll be {age + 30} years old.")
    
    except ValueError:
        print("Please enter a valid age.")
