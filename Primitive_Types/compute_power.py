# Write a program that take a double x and an integer y
# we are allowed to ignore overflowm and underflow
# book hint:
#       'Exploit mathematical properties of exponentiations'
#   First assume y will be nonnegative 
#   we could use a brute force method x^2 = X * X
#   but this algorithm results in O(2^n)
#   where n is the number of bits needed to represent y
#     
#   the key to efficiency is to try and get more work done in each
#   iteration similar to the previous problem in no_multiply
#   lets say we have x = 1.1 y=21
#   instead of doing 1.1 ^ 21 as previously mentioned
#   we could, multiple 1.1 by (1.1)^2 = 1.21, 10 times (11 multiplications)
#   
#   
# #

def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0/x 
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result