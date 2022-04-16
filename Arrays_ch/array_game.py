# write a program that takes an array of n integers, where A[i] denotes the maximum number
# you can advance from index i, the function will return wether you can reach the end 
# of the array or not
# 
# if we try to go as far as possible from each index we are on, 
# it will be easy to skip big numbers hidden in between
# ex:
#   arr= [2,4,1,0,2,0,1]
# with this logic we're bound to fail, we'd go from 2>1>0 
# the book suggest we iterate through all entries in the Array
# as we iterate we keep track of our furthest reaching[i] from that index
# 
# #

def can_reach_end(A):
    furthest_reaching_so_far, last_index = 0, len(A) -1
    i = 0
    while i <= furthest_reaching_so_far and furthest_reaching_so_far <= last_index:
        furthest_reaching_so_far = max(furthest_reaching_so_far, A[i] + i)
        i+= 1
    return furthest_reaching_so_far >= last_index
