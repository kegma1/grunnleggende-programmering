# Write a program that reads in an investment amount, the annual interest rate, and the number of years, and then displays the future investment value using the following formula:
# futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ^ numberOfMonths
# For example, if you enter the amount 1000.56, an annual interest rate of 4.25%, and the number of years as 1, the future investment value is 1043.33. Here is a sample run:
# Enter investment amount: 1000.56
# Enter annual interest rate: 4.25
# Enter number of years: 1
# Accumulated value is 1043.92

investment = float(input("Enter investment amount: "))
#investment = 1000.56
annualInterest = float(input("Enter annual interest rate: "))
#annualInterest = 4.25
numOfYears = float(input("Enter number of years: "))
#numOfYears = 1

numOfMounths = numOfYears * 12
mounthlyIntrest = (annualInterest / 100) / 12

accumulatedValue = investment * (1 + mounthlyIntrest) ** numOfMounths
print(f"Accumulated value is {accumulatedValue:.2f}")