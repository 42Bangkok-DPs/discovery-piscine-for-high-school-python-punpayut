# Function to display the multiplication table
def display_multiplication_table(number):
    for i in range(10):
        print(f"{i} x {number} = {i * number}")

# Main program
if __name__ == "__main__":
    try:
        # Accept input from the user
        number = int(input("Enter a number: "))
        
        # Display the multiplication table
        display_multiplication_table(number)
    
    except ValueError:
        print("Please enter a valid integer.")
