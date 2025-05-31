# User Input for Financial Details
monthly_income_str = input("Enter your monthly income: ")
monthly_income = int(monthly_income_str)

monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = int(monthly_expenses_str)

# Calculate Monthly Savings
# Since income and expenses are integers, monthly_savings will be an integer.
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
# The formula: (Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
# The term (Monthly Savings * 12 * 0.05) results in a float.
# The sum will then be a float.

annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * 0.05 # This can be float

projected_savings_calculation = annual_savings_without_interest + interest_earned
projected_savings_after_year = int(projected_savings_calculation)

# Output Results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings_after_year}.")