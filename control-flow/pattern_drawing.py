size_str = input("Enter the size of the pattern: ")

try:
    size = int(size_str)
    if size <= 0:
        print("Please enter a positive integer for the size.")
        exit()
except ValueError:
    print("Invalid input. Please enter a positive integer for the size.")
    exit() # Exit if conversion fails


row_count = 0
while row_count < size:
    for _ in range(size): # Inner loop for columns
        print("*", end="")
    print() # Moves to the next line after printing all asterisks in a row
    row_count += 1