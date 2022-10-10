def formatList(list) -> str:
    if len(list) == 1:
        return list[0]

    finalString = ""
    finalString += " and " + list[-1]
    finalString = ", ".join(list[0:-1]) + finalString
    return finalString

def main():
    userList = []
    userInput = " "

    while userInput != "":
        userInput = input("Enter an item (blank to quit): ")
        userList.append(userInput)
    userList.pop()
    print(f"The items are {formatList(userList)}.")

if __name__ == "__main__":
    main()