list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print([x for x in list1 if x > 10 and x % 2 == 0])

x = [10, [3.141, 20, [30, 'apple', 2.718]], 'banana']
print(x[1][2][1:])

x = [10, [3.141, 20, [30, 'apple', 2.718]], 'banana']
print(x[1][2][1][-1])