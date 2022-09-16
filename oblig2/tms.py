def format(seconds:int)->str:
    tim = seconds // (60*60)
    if tim > 24:
        while tim >= 24:
            tim -= 24
    seconds = seconds % (60*60)
    min = seconds // (60) 
    seconds = seconds % (60)
    return f"{tim:02}:{min:02}:{seconds:02}"

userInput = int(input("Enter total seconds: "))
print(f"The hours, minutes, and seconds for total seconds {userInput} is {format(userInput)}")