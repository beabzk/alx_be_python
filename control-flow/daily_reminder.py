task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for easier comparison
time_bound_input = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase

# Determine if time_bound based on input
time_bound = True if time_bound_input == "yes" else False

reminder_message = ""

match priority:
    case "high":
        if time_bound:
            reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a high priority task." # Fallback if not explicitly defined for non-time-bound high
    case "medium":
        if time_bound:
            reminder_message = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a medium priority task." # Fallback
    case "low":
        if time_bound:
            # The example for low and time-bound isn't given, but we can infer a similar structure
            reminder_message = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
        else:
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level entered. Please choose high, medium, or low."

print(reminder_message)