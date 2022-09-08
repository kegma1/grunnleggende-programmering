# In this exercise, use the following variables: i, lo, hi, and result.
# Assume that lo and hi each are associated with an integer and that result refers to 0.
# Write a while loop that adds the integers from lo up through hi (inclusive), and associates the sum with result.
# Your code should not change the values associated with lo and hi. Also, just use these variables: i, lo, hi, and result.

lo = 1
hi = 10
i = lo
total = 0

while i <= hi:
    total += i
    i += 1