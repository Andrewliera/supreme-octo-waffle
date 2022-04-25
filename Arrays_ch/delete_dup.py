# write a program that takes in a sorted Array as an input
# and returns the array with duplicate elements removed from it
# finally the remaining elements from the array will be shifted left to swap empty indecies to the right of last stored index 
# Book Ex: input = [1,3,3,5,6,7,13,13,13]
#         output = [1,3,5,6,7,13,0,0,0]  
#                       
# the book describes that there are no requirements for the values stored beyond the last valid element              
# 
# the brute for method is straight forward, iterate through the array
# while comparing if elements A[i] == A[i + 1], if it is  
# we will shift all elements A[i + 2] to the left by one 
# however with this approach, if all entries are equal then the big O == O(n^2)
# the number of shifts is (n -1)+(n -2)+...+2+1 
# 
# #
def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
        return write_index