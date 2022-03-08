# calculating the parity of a word
# a binary word is 8-16 bits(thanks google)
# the binary word will equal odd if there are an odd number of 1's 
#  1 == 1011  || 0 == 10001000 
# this is one of the ways that we can detect single bit errors in data or storage


def parity(x):
    result = 0
    while x:
        result ^= x&1
        x >>= 1
    return result


def parityTwo(y):
    temp = 0
    while y:
        temp ^= 1
        y &= y - 1 #Drops the lowest significant bit
    return temp

