# Write a function that returns the sum of all the elements in a specified column in a matrix using the following header:
# def sumColumn(m, columnIndex):
# Write a test program that reads a 3 × 4 matrix and displays the sum of each column. Note that the matrix is entered by rows and 
# the numbers in each row are separated by a space in one line.
# Sample Run
# Enter a 3-by-4 matrix row 0: 1.5 2 3 4
# Enter a 3-by-4 matrix row 1: 5.5 6 7 8
# Enter a 3-by-4 matrix row 2: 9.5 1 3 1
# Sum of the elements for column 0 is 16.5
# Sum of the elements for column 1 is 9.0
# Sum of the elements for column 2 is 13.0
# Sum of the elements for column 3 is 13.0

def sumColumn(m, columnIndex):
    accumulator = 0
    for rowIndex in range(0, len(m)):
        accumulator += m[rowIndex][columnIndex]
    return accumulator

matrix = []
for i in range(3):
    matrix.append([float(x) for x in input(f"Enter a 3-by-4 matrix row {i}: ").split(" ")])
for i in range(4):
    print(f"Sum of the elements for column {i} is {sumColumn(matrix, i)}")