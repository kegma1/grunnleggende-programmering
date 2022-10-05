# Write the following function that returns the location of the largest element in a two-dimensional list:
# def locateLargest(a):
# The return value is a one-dimensional list that contains two elements. These two elements indicate the row 
# and column indexes of the largest element in the two-dimensional list. Write a test program that prompts the 
# user to enter a two-dimensional list and displays the location of the largest element in the list. Note that 
# the matrix is entered by rows and the numbers in each row are separated by a space in one line. Here is a sample run:
# Sample Run
# Enter the number of rows in the list: 3
# Enter a row: 23.5 35 2 10
# Enter a row: 4.5 3 45 3.5
# Enter a row: 35 44 5.5 11.6
# The location of the largest element is at (1, 2)



def locateLargest(a):
    largestIndexes = []
    for row in a:
        (_, index) = max((x, i) for (i, x) in enumerate(row)) 
        largestIndexes.append(index)
    biggestInRow = [(a[i][x], i,x) for i, x in enumerate(largestIndexes)]
    return biggestInRow
    
    

print(locateLargest([
    [23.5, 35, 2, 10],
    [4.5, 3, 45, 3.5],
    [35, 44, 5.5, 11.6]
]))