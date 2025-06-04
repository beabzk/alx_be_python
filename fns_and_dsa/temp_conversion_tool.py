# Define Global Conversion Factors
# These are the multiplicative factors used in the standard conversion formulas
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
OFFSET = 32 # The offset used in temperature conversions

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using global factors."""
    # Celsius = (Fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using global factors."""
    # Fahrenheit = (Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    return fahrenheit

def main():
    try:
        temp_str = input("Enter the temperature to convert: ")
        temperature = float(temp_str)
    except ValueError:
        # "raise an error 'Invalid temperature. Please enter a numeric value.'"
        # Interpreted as printing an error message to the user, not raising a Python exception.
        print("Error: Invalid temperature. Please enter a numeric value.")
        return # Exit the function

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()