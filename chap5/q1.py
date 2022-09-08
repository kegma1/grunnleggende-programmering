# Use the variables k and total to write a while loop that computes 
# the sum of the squares of the first 50 counting numbers, and associates 
# that value with total. 
# Thus your code should associate 1*1 + 2*2 + 3*3 +... + 49*49 + 50*50 with 
# total. Use no variables other than k and total.

k = 50
total = 0
while k > 0:
    total += k * k
    k -= 1

