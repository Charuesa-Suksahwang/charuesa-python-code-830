"""
Personal Finance Calculator
Student: [Charuesa Suksahwang]
Date: [27/07/2025]
Purpose: Calculate monthly budget and savings
"""

monthly_income = float(input("User's monthly income in THB: "))
rent_cost = float(input("Monthly rent/housing cost: "))
food_budget = int(input("Monthly food budget in THB: "))  
transportation_cost = float(input("Monthly transportation expenses: "))
entertainment_budget = int(input("Monthly entertainment budget: "))
emergency_fund_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percentage to invest: "))

total_fixed_expenses = rent_cost + transportation_cost
total_variable_expenses = food_budget + entertainment_budget
total_expenses = total_fixed_expenses + total_variable_expenses
remaining_income = monthly_income - total_expenses
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)
available_for_savings = remaining_income - emergency_fund_percent - investment_amount
expense_ratio = (total_expenses / monthly_income) * 100
print()
print("===MONTHLY BUDGET REPORT===")
print(f"Income:{monthly_income:.2f}THB")
print(f"Fixed Expensses:{total_fixed_expenses:.2f}THB")
print(f"Variable Expenses:{total_variable_expenses:.2f}THB")
print(f"Remaining:{remaining_income:.2f}THB")
print()
print("===SAVINGS BREAKDOWN===")
print(f"Emergency Fund(10%):{emergency_fund_amount:.2f}THB")
print(f"Available for Savings:{available_for_savings:.2f}THB")
print()
print("==ANALYSIS==")
print(f"Expense Ratio:{expense_ratio:.2f}%")
