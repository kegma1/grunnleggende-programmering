def formatList(list) -> str:
    if len(list) == 1:
        return list[0]
    else:
        finalString = ""
        finalString += " and " + list[-1]
        finalString = ", ".join(list[0:-1]) + finalString
        return finalString

userList = []
userInput = " "

while userInput != "":
    userInput = input("Enter an item (blank to quit): ")
    userList.append(userInput)
userList.pop()
print(f"The items are {formatList(userList)}.")