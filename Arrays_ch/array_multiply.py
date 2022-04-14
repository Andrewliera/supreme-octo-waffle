# write a program that takes two arrays representing intengers
# and return an array representing theirn products
# just like in the "increment an integer represented as an array by 1" problem
# we could extract the integers from the arrays multiple and encode
# but this "brute force solution" has overflow issues
# book solution: use a school algorithm for multiplication 
# 
#   ->   123 * 987    =>  (7 * (123)) + (80 *(123)) + (900 * (123)) = 121401  
#                                                                   
# 
# #

def array_multiply(num1, num2): 
    sign = -1 if(num1[0] < 0 ) ^ (num2[0] < 0) else 1 
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[ i + j + 1] // 10
            result[i + j + 1] %= 10
    #the author uses the code below to remove leading zeros
    result = result[next((i for i, x in enumerate(result)
        if x != 0), len(result)):] or [0]
    return sign * result[0] + result[1:]
temp1 = [2,2,0]
temp2 = [1,0]
array_multiply(temp1,temp2)