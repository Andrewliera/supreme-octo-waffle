# solution credit/ explenation -> Pen&paper programming
#write a variant that use bitwise operators, equality checks, and Boolean operators 
#to do the following in O(1) time
#right propagate the rightmost set bit
#compute x mod a power of two -> returns 13 for 77 mod 64
#Test if x is a power of 2, evaluates true for x = 1,2,4,8. false otherwise 

# right propogate right most set bit
#        (00100000)
#      or(  011111)
#       ------------
#         (01011111)

def propagate_rightmost_bit(x):
    return x | (x - 1)



# Part 2: expression that computes x mod a w/ power of 2 
# 77 % 64 = 13

# 77 -> (01001101)      13 -> (1101)
# 64 -> (01000000)

#   01001101  => 77             
# & 00111111  => (64 - 1) = 63
# ------------
#   00001101  = > 13

def compute_x_mod_a(x, power):
        return x & ((1 << power) - 1)

# part 3
# test if x is a power of 2 if it is return true else return false
# there will only be one bit set for number with a power of two
#   0010 => 2     00001000 = > 8       = x
#  &0001         &00000111             = (x -1)
# -------       -----------
#   0000          00000000

def isPowerOftwo(x):    
    return (x & (x - 1)) == 0