# Main program
if __name__ == "__main__":
    while True:
        # Accept user input
        user_input = input("What you gotta say? : ")
        
        # Check if the user entered "STOP"
        if user_input == "STOP":
            break
        
        # Otherwise, respond and continue the loop
        print("I got that! Anything else?")
