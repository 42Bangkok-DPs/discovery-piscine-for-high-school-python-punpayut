#!/usr/bin/env python3

# Main program
if __name__ == "__main__":
    try:
        # Ask the user for a number
        number = float(input("Give me a number: "))
        
        # Check if the number is an integer or a decimal
        if number.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    
    except ValueError:
        print("Please enter a valid number.")
