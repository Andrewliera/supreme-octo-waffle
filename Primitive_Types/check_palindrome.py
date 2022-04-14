# Write a program that checks if a decimal integer is a palindrome
# A palindromic string is one which reads the same forward and backwards
# first, negative numbers are not palindromic 
# since it begins with a -
# book  hint: we could extract the least significant digit(like with def reverse_digits)
# a brute force approach : we could iterate from the beginning and end of the string inwards  
# and return false if there is a missmatch:
#  
# most sig.     least sig.
#       |       |
#       v       v
#       123454321 
# 
#   the better approach the book describes is 
#   extracting digits
#   similar to rever_digits
#   we can extract the least significant bit with x mod 10
#   but we can also extract the most significant bit 
#   with the formula x/10^(n-1) 
#   we iteratively compare digits, and in each iteration extract the digits
#
#   |       |
#   v       v
#   123454321
#
#   v     v
#   2345432
#
#   v   v
#   34543
#
# #
import math
def is_palindrome(x):
    if x <= 0:
        return x == 0 
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 **(num_digits - 1)
    for i in range(num_digits // 2 ):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True