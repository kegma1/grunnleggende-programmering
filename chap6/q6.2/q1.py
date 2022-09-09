# Write the definition of a function typing_speed, that receives two parameters. 
# The first is the number of words that a person has typed (an integer greater than or equal to zero) 
# in a particular time interval. The second is the length of the time interval in seconds 
# (an integer greater than zero). The function returns the typing speed of that person in words per minute (a float).

def typing_speed(words, interval):
    # Get words per second and convert it to minutes
    return words / interval * 60