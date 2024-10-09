import sys

# Function to display all multiplication tables
def display_tables():
    for i in range(11):
        row = " ".join(str(i * j) for j in range(11))
        print(f"Table de {i}: {row}")

# Main program
if __name__ == "__main__":
    # Check if any arguments are provided
    if len(sys.argv) > 1:
        print("none")
    else:
        display_tables()
