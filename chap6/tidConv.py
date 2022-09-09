# Write a function that converts milliseconds to hours, minutes, and seconds using the following header:
# def convertMillis(millis):
# The function returns a string as hours:minutes:seconds.
# For example, convertMillis(5500) returns the string 0:0:5, convertMillis(100000) 
# returns the string 0:1:40, and convertMillis(555550000) returns the string 154:19:10.
# Write a test program that prompts the user to enter a value for milliseconds and 
# displays a string in the format of hours:minutes:seconds.

# Sample Run
# Enter time in milliseconds: 555550000
# 154:19:10

def convertMillis(millis):
    tim = millis // (60*60*1000)
    millis = millis % (60*60*1000)
    min = millis // (60*1000) 
    millis = millis % (60*1000)
    sec = millis // 1000
    return f"{tim}:{min}:{sec}"

userMillis = int(input("Enter time in milliseconds: "))
print(convertMillis(userMillis))