# Given an array of integers 
# sort the array so that even entries appear before odd entries
# array_A = [2,3,4,5] -> new_array_A = [2,4,3,5]
#
# the book explains that when working with array we should use the fact that 
# we can operate efficiently on both ends
# and solves this problem by breaking the array into 3 subarrays
# even, odd and unsorted. the author at first leaves the original array in unsorted,
# while the even and odd arrays are empty
# then uses swaps to shrink unsorted, while expanding even and odd
# #

def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1