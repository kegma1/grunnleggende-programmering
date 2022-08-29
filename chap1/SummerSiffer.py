num = int(input("Enter a number for 0-1000: "))
if num > 1000:
    exit()
digit1 = num % 10
digit2 = (num % 100) // 10
digit3 = (num % 1000) // 100
digit4 = num // 1000

sum = digit1 + digit2 + digit3 + digit4
print(sum)