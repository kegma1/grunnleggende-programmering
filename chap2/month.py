# (Find the number of days in a month)
# Write a program that prompts the user to enter the month and year and displays the number of days in the month. For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
# Sample Run 1
# Enter a month in the year (e.g., 1 for Jan): 4
# Enter a year: 2005
# April 2005 has 30 days
# Sample Run 2
# Enter a month in the year (e.g., 1 for Jan): 2
# Enter a year: 2006
# February 2006 has 28 days
# Sample Run 3
# Enter a month in the year (e.g., 1 for Jan): 2
# Enter a year: 2000
# February 2000 has 29 days

userMonth = int(input("Enter a month in the year (e.g., 1 for Jan): "))
userYear = int(input("Enter a year: "))

isLeapYear = userYear % 4 == 0
#               jan, feb, mar, apr, mai, jun, jul, aug, sep, oct, nov, des
daysInMonths = [31,  28,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31]
selectedMonth = daysInMonths[userMonth - 1]

MonthName = ""
if userMonth == 1:
    MonthName = "January"
elif userMonth == 2:
    MonthName = "February"
elif userMonth == 3:
    MonthName = "March"
elif userMonth == 4:
    MonthName = "April"
elif userMonth == 5:
    MonthName = "May"
elif userMonth == 6:
    MonthName = "June"
elif userMonth == 7:
    MonthName = "July"
elif userMonth == 8:
    MonthName = "August"
elif userMonth == 9:
    MonthName = "September"
elif userMonth == 10:
    MonthName = "October"
elif userMonth == 11:
    MonthName = "November"
elif userMonth == 12:
    MonthName = "December"

if userMonth == 2 and isLeapYear:
    selectedMonth += 1
print(f"{MonthName} {userYear} has {selectedMonth} days")
