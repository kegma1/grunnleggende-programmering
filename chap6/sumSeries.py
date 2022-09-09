# Write a function to compute the following series:
# m(i) = 1/2 + 2/3 + ... + i/(i+1)
# Write a test program that displays the following table:
# i                   m(i)
# 1                 0.5000
# 2                 1.1667
# ...
# 19                16.4023
# 20                17.3546

def m(i):
    if i == 0:
        return i
    else:
        return m(i - 1) + i / (i + 1)

for i in range(1, 20):
    print(f"{i}\t{m(i):.4f}")