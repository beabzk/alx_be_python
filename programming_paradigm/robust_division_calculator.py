def safe_divide(numerator, denominator):
    """
    Performs division and handles potential errors.

    Args:
        numerator (str or float or int): The number to be divided.
        denominator (str or float or int): The number to divide by.

    Returns:
        str: A message with the result of the division or an error message.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."