num = int(input("Enter a 3 digit number: "))

if num >= 100 and num < 1000:
    firstDigit = num // 100
    lastDigit = num % 10

    if firstDigit == lastDigit:
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
    exit()
print(f"{num} is not a 3 digit number!!")