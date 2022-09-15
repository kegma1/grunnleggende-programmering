def decToBin(num: int) -> str: # inspiration fra htt
    ps://www.cuemath.com/numbers/decimal-to-binary/
    if num == 0:
        return ""
    else:
        return decToBin(num // 2) + str(num % 2)

userInput = int(input("Enter a decimal number between 0 and 15: "))
# if userInput < 0 or userInput > 15:
#     exit()
print(f"The binary number for {userInput} is {decToBin(userInput)}")