#!/usr/bin/env python3

# Main program
if __name__ == "__main__":
    # Ask the user for a string
    user_input = input("Give me a string: ")
    
    # Switch uppercase letters to lowercase and vice versa
    switched_string = user_input.swapcase()
    
    # Display the transformed string
    print(switched_string)
