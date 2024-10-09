#!/usr/bin/env python3
import math

# Main program
if __name__ == "__main__":
    try:
        # Ask the user for a number
        number = float(input("Give me a number: "))
        
        # Round up the number
        rounded_number = math.ceil(number)
        
        # Display the rounded number
        print(rounded_number)
    
    except ValueError:
        print("Please enter a valid number.")
