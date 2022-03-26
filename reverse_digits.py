# write a program that take an integer
# and return it an a reverse order
# brute force method convert to string 
# we can actually not use string at all here
# by using mod 10 can extract the least significant digit of the int,
# we can then use result and x_remain to keep track of our number at each while iteration
# 
# a solid explentation by Joseph Boss for the //=
# 
# in python -> 7 / 4 = 1.75
#              7 // 4 = 1
# 
# 
# #
def reverse(x):
    result = 0 
    x_ramain = abs(x)
    while x_remain:
        result = result * 10 + x_ramain % 10 
        x_ramain //= 10
    return -result if x < 0 else result