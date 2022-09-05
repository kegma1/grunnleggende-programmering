# An ISBN-10 (International Standard Book Number) consists of 10 digits: d1d2d3d4d5d6d7d8d9d10. The last digit, d10, is a checksum, which is calculated from the other nine digits using the following formula:
# (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
# If the checksum is 10, the last digit is denoted as X according to the ISBN-10 convention. Write a program that prompts the user to enter the first 9 digits and displays the 10-digit ISBN (including leading zeros).
# Sample Run 1
# Enter the first 9 digits of an ISBN as a string: 3601267
# Incorrect input. It must have exact 9 digits
# Sample Run 2
# Enter the first 9 digits of an ISBN as a string: 013601267
# The ISBN-10 number is 0136012671
# Sample Run 3
# Enter the first 9 digits of an ISBN as a string: 013031997
# The ISBN-10 number is 013031997X



userInput = input("Enter the first 9 digits of an ISBN as a string: ")
if not len(userInput) >= 9 or not len(userInput) < 10:
    print("Incorrect input. It must have exact 9 digits")
    exit()

zero = ord("0")
checksum = 0
for i, d in enumerate(userInput):
    digit = ord(d) - zero
    checksum += digit * (i + 1)
checksum %= 11

if checksum == 10:
    userInput += "X"
else:
    userInput += str(checksum)

print(f"The ISBN-10 number is {userInput}")
    