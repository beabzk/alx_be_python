task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder_message = ""

match priority:
    case "high":
        if time_bound == "yes":
            reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        if time_bound == "yes": # Matches pattern
            reminder_message = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a medium priority task."
    case "low":
        if time_bound == "yes": # Matches pattern
            reminder_message = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
        else: # This implies time_bound is "no" or something else
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")
        exit() # Exit if priority is invalid to avoid printing an empty reminder_message

print(reminder_message)