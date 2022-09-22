# Write a function that checks whether two words are anagrams. Two words are anagrams if they contain the same letters. 
# For example, silent and listen are anagrams. The header of the function is:
# def isAnagram(s1, s2):
# (Hint: Obtain two lists for the two strings. Sort the lists and check if two lists are identical.)
# Write a test program that prompts the user to enter two strings and checks whether they are anagrams.
# Sample Run 1
# Enter a string s1: silent
# Enter a string s2: listen
# silent and listen are anagrams
# Sample Run 2
# Enter a string s1: split
# Enter a string s2: lisp
# split and lisp are not anagrams

def isAnagram(s1, s2):
    s1Sorted = ''.join(sorted(s1))
    s2Sorted = ''.join(sorted(s2))

    return s1Sorted == s2Sorted

s1 = input("Enter a string s1: ")
s2 = input("Enter a string s2: ")

if isAnagram(s1, s2):
    print(f"{s1} and {s2} are anagrams")
else:
    print(f"{s1} and {s2} are not anagrams")