# Write a program that prompts the user to enter a point (x, y) and checks whether the point is within the rectangle centered at (0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and (6, 4) is outside the rectangle, as shown in Figure 3.7b in the Programming Exercise from the Book section.
# Hint: A point is in the rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and its vertical distance to (0, 0) is less than or equal to 5.0 / 2. Test your program to cover all cases.
# Sample Run 1
# Enter the x-coordinate of the point: 2
# Enter the y-coordinate of the point: 2
# Point (2.0, 2.0) is in the rectangle
# Sample Run 2
# Enter the x-coordinate of the point: 6
# Enter the y-coordinate of the point: 4
# Point (6.0, 4.0) is not in the rectangle

userX = float(input("Enter the x-coordinate of the point: "))
userY = float(input("Enter the y-coordinate of the point: "))

topX = 10 / 2
topY = 5 / 2

isInRectangle = userX >= -topX and userX <= topX and userY >= -topY and userY <= topY

if isInRectangle:
    print(f"Point ({userX}, {userY}) is in the rectangle")
else:
    print(f"Point ({userX}, {userY}) is not in the rectangle")