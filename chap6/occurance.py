# Write a function that finds the number of occurrences of a specified character in the string using the following header:
# def count(s, ch):
# For example, count("Welcome", 'e') returns 2. The str class has the count method. Implement your function without using 
# the count method. Write a test program that reads a string and a character and displays 
# the number of occurrences of the character in the string.

# Sample Run
# Enter a string: Welcome to Python
# Enter a character: o
# o appears in Welcome to Python 3 times

def count(s, ch):
    c = 0
    for elm in s:
        if elm == ch:
            c += 1
        else:
            pass
    return c

userString = input("Enter a string: ")
userChar = input("Enter a character: ")

print(f"{userChar} appears in {userString} {count(userString, userChar)} times")