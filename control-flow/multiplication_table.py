number_str = input("Enter a number to see its multiplication table: ")

try:
    number = int(number_str)
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit() # Exit if conversion fails

for i in range(1, 11): # Iterates from 1 to 10 (inclusive)
    product = number * i
    print(f"{number} * {i} = {product}")