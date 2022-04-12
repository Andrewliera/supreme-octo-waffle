#write a program that takes as input an array of digits 
# encoding a nonnegative decimal integer D
# and updates the array to represent the integer D + 1
# 
# book hint: expirement with concrete example
# brute force approach: convert array into integer -> increment 
# -> convert integer to array
# but the book explains this solution will fail when 
# encoding ints outside of its range of whichever language you are using
# 
# instead we can 
# add digits starting with the least significant 
# and push the carry
# we will increment 0 -> 9, then reset to 0 with a carry of 1 
#       
#     LSD
#      v 
# <1,2,9> -> <1,3,0>
# 
# #

def plus_one_fun(Arr):
    Arr[-1] += 1
    for i in reversed(range(1, len(Arr))):
        if Arr[i] != 10:
            break
            Arr[i] = 0
            Arr[i - 1] += 1
        if Arr[0] == 10:#"with a carry out bit we need one more digit to store the result, a slick way to do this is to append a 0 at the end of the array" -E.P.I Author 
            Arr[0] = 1
            Arr.append(0)
        return Arr