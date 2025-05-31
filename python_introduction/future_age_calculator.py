# Prompt the user for their current age
current_age_str = input("How old are you? ")

# Convert the input string to an integer
current_age = int(current_age_str)

# Calculate age in 2050 (current year 2023, so 2050 - 2023 = 27 years difference)
years_to_add = 27
future_age = current_age + years_to_add

# Print the user's age in 2050
print(f"In 2050, you will be {future_age} years old.")