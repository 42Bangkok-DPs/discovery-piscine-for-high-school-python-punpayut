#!/usr/bin/env python3

# Main program
if __name__ == "__main__":
    try:
        # Ask the user for two numbers
        num1 = float(input("Give me the first number: "))
        num2 = float(input("Give me the second number: "))
        
        print("Thank you!")
        
        # Perform and display the results of addition, subtraction, division, and multiplication
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} / {num2} = {num1 / num2}")
        print(f"{num1} * {num2} = {num1 * num2}")
    
    except ValueError:
        print("Please enter valid numbers.")

