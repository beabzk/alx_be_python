import datetime

def display_current_datetime():
    """
    Displays the current date and time formatted.
    """
    current_datetime_obj = datetime.datetime.now()
    # Save the current date and time in a variable (though it's used immediately for formatting)
    current_date_and_time_str = current_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_and_time_str}")
    return current_datetime_obj # Return the object for potential further use if needed

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates a future date.
    """
    current_date_obj = datetime.datetime.now().date() # Get current date part

    while True:
        try:
            number_of_days_str = input("Enter the number of days to add to the current date: ")
            number_of_days = int(number_of_days_str)
            if number_of_days < 0:
                print("Please enter a non-negative number of days.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    time_delta = datetime.timedelta(days=number_of_days)
    future_date_obj = current_date_obj + time_delta
    # Save the future date in a variable (though it's used immediately for formatting)
    future_date_str = future_date_obj.strftime("%Y-%m-%d")
    print(f"Future date: {future_date_str}")
    return future_date_obj # Return the object for potential further use

def main():
    display_current_datetime()
    print() # Add a newline for better readability
    calculate_future_date()

if __name__ == "__main__":
    main()