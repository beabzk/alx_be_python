num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

# Attempt to convert inputs to numbers
try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("Invalid input. Please enter numeric values for numbers.")
    exit() # Exit if conversion fails

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _: # Handles any operation not listed above
        print("Invalid operation selected. Please choose from +, -, *, /.")