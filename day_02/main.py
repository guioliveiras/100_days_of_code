print("Welcome to the tip calculator.")

# Inputs
bill = float(input("What was the total bill? "))
percentage = int(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

# Calculation
result = (bill/people)*(1+percentage/100)
result = round(result, 2)

# Output
print(f"Each person should pay: ${result}")
