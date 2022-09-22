# (Sorted?)
# Write the following function that returns True if the list is already sorted in increasing order:
# def isSorted(lst):
# Write a test program that prompts the user to enter a list of numbers separated by a space in one line and displays whether the list is sorted or not. Here is a sample run:
# Sample Run 1
# Enter list: 1 1 3 4 4 5 7 9 10 30 11
# The list is not sorted
# Sample Run 2
# Enter list: 1 1 3 4 4 5 7 9 10 30 
# The list is already sorted

def isSorted(lst):
    i = 0
    while i <= len(lst):
        if i == len(lst) - 1:
            break
        if lst[i] <= lst[i + 1]:
            i += 1
            continue
        else: 
            return False
        i += 1
    return True

userInput = [int(x) for x in input("Enter list: ").split(" ")]

if isSorted(userInput):
    print("The list is already sorted")
else:
    print("The list is not sorted")
