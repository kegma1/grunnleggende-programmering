# Write the definition of a function power_to, which receives two parameters. 
# The first is a float and the second is an integer. The function returns a float.
# If the second parameter is negative, the function returns zero. 
# Otherwise it returns the value of the first parameter raised to the power of the second.

def power_to(base, exponent):
    if exponent < 0:
        return 0.0
    return base ** exponent
