# Return the reversal of an integer, e.g. reverse(456) returns 654
def reverse(number:int) -> int:
    reversed_number = 0

    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number

# Return true if number is a palindrome
def isPalindrome(number:int) -> bool:
    return number == reverse(number)


num = int(input("Enter an integer: "))
if isPalindrome(num):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")