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

userMounth = int(input("Enter a month in the year (e.g., 1 for Jan): "))
userYear = int(input("Enter a year: "))

isLeapYear = userYear % 4 == 0
#               jan, feb, mar, apr, mai, jun, jul, aug, sep, oct, nov, des
daysInMounths = [31,  28,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31]
selectedMounth = daysInMounths[userMounth - 1]

mounthName = ""
if userMounth == 1:
    mounthName = "January"
elif userMounth == 2:
    mounthName = "February"
elif userMounth == 3:
    mounthName = "March"
elif userMounth == 4:
    mounthName = "April"
elif userMounth == 5:
    mounthName = "May"
elif userMounth == 6:
    mounthName = "June"
elif userMounth == 7:
    mounthName = "July"
elif userMounth == 8:
    mounthName = "August"
elif userMounth == 9:
    mounthName = "September"
elif userMounth == 10:
    mounthName = "October"
elif userMounth == 11:
    mounthName = "November"
elif userMounth == 12:
    mounthName = "December"

if userMounth == 2 and isLeapYear:
    selectedMounth += 1
print(f"{mounthName} {userYear} has {selectedMounth} days")
