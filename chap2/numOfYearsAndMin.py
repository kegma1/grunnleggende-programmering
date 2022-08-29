# Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. For simplicity, assume a year has 365 days. Here is a sample run:
# Enter the number of minutes: 1_000_000_000
# 1000000000 minutes is approximately 1902 years and 214 days

userInput = int(input("Enter the number of minutes: "))
#userInput = 1_000_000_000
numOfYears = userInput // 60 // 24 // 365
numOfDays = userInput // 60 // 24 % 365
print(f"{userInput} minutes is approximately {numOfYears} years and {numOfDays} days")