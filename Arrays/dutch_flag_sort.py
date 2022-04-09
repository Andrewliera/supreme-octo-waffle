# write a program that takes an array A, and an index i into A 
# and rearranges the elements so that all elements less than A[i]
# appear first followed by elements equal to the pivot(A[i])  
# and then elements greater than A[i]
# 
# book hint: Think about partition step in quicksort 
# > in other words the book is asking us to solve the problem with
# a quick sort algorithm 
# if element A[j] is less than our pivot swap them
# 
# 
# #

RED, WHITE, BLUE = range(3)

def dutch_flag_sort(pivot_index, A):
    pivot = A[pivot_index]
    for i in range (len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot: 
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(len(A))):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
# we pass the elements in the function twice 
# first -> for i in range(len(A)):
#   second -> for j in range(...)
# so the above function has a time complexity of O(n^2)

def dutch_flag_sort_two(pivot_index, A):
    pivot = A[pivot_index]
    smaller = 0 
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
# this time the algorithm seperated elements in 1 pass rather than a nested one
# for O(n)