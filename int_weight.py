# Find Closest integer with the same bit
#
# define the wieght of a nonnegative integer x to be
#the number of bits set to 1 in its binary form
#       ex:     (92)(base-10) -> (1011100)(base-2) -> (4)(wight)
#write a program that takes x as a nonnegative integer
# and returns a number y as the weight of x 
# however the difference of |y - x| is as small as possible
# if x = 6, then we return 5
# 
# the book describes that, 
# if we try to focus on swapping LSBs like in the previous problems
# we might get some correct numbers at first but we will get 
# incorrect results for some test cases.
# 
# assume, we swap the bit at index k1
# and flip the bit at k2, k1>k2 
# then, the absolute value of the original int and the new one is
# (2^(k1) - 2^(k2))
# to apply this into the function we want to pick the smallest k1
# and the closest k2 != k1 however is ~k1  #
# 
# 
# -> we are looking for the 2 rightmost consecutive bits that are different
# #

def int_bit_weight(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS -1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (i << i) | (i << (i + 1))
            return x
    raise ValueError('All bits are 0 or 1')