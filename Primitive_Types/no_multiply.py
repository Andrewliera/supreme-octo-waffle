#compute x * y without using without arithmatic operators 
# we are allowed to use:
# assignment
# bitwise >>, <<, |, &, ~, ^
# equality checks and boolean combinations
#   brute force -> repeated addition
#   5*3 => 0 + 5, 5 + 5 , 10+5 
#   the book describes that the the Algortihm Taught in grade school
#   where it does not use repeated addition but uses a shift and add method 
#   with a better time complexity
#   by going through each LSB at a time,
#      6        10          
#   (0110) * (1010)   
#              =>       1st lsb(of 6) -> 01[1]0 so we shift 1010 by 1 
#                                                       10100 
#                                                      
#
#               =>      2nd lsb(of 6) -> 0[1]10 so we shift 1010 by 2
#                                                          101000 
#           
#             10100 + 101000
#              ---------                                      
#               111100                                       
#                                           

def no_arith_mult(x,y):
    def add(a, b):
        running_sum, carryIn, k, temp_a, temp_b = 0 , 0 , 1, a , b
        while temp_a or temp_b:
            ak = a & k
            bk = b & k
            carryOut = (ak & bk) | (ak & carryIn) | (bk & carryIn)
            running_sum |= ak ^ bk ^ carryIn
            carryIn, k, temp_a, temp_b = (
                carryOut << 1, k << 1, temp_a >> 1, temp_b >> 1)
            return running_sum | carryIn

        running_sum = 0 
        while x: #examins each bit of x
            if x & 1:
                running_sum = add(running_sum, y)
            x, y = x >> 1, y << 1
            return running_sum