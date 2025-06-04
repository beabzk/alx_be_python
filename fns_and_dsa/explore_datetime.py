from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time formatted.
    Saves the formatted current date and time string in the 'current_date' variable.
    """
    current_datetime_obj = datetime.now()
    # Requirement: "save the current date inside a current_date variable"
    # which is then printed
    current_date = current_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    """
    Prompts for a number of days, calculates the future date,
    prints it, and returns the formatted future date string.
    Saves the future date datetime object in the 'future_date' variable.
    """
    current_datetime_for_calc = datetime.now() # Use current datetime for calculation

    while True:
        try:
            number_of_days_str = input("Enter the number of days to add to the current date: ")
            number_of_days = int(number_of_days_str)
            if number_of_days < 0: # Added basic validation
                print("Please enter a non-negative number of days.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    time_delta_obj = timedelta(days=number_of_days)
    
    # Requirement: "saves the future date inside a future_date variable"

    future_date = current_datetime_for_calc + time_delta_obj
    
    formatted_future_date_str = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date_str}")
    
    return formatted_future_date_str

def main():
    display_current_datetime()
    print()
    calculate_future_date()

if __name__ == "__main__":
    main()