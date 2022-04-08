# create a random number generator that generates:
# a random integer i between a and b
# all values in a and be should be equally likely
# book hint: how would you mimic a three sided coin         <- ~w h a t ?
# with a two sided coin?                                          
# 
# 
# 
# 
# 
# 
# #
def uniform_random(lower_bound, upper_bound):
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i =  0 , 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | randrange(upper_bound, lower_bound, 1)
            i += 1
        if result < number_of_outcomes:
            break
        return result + lower_bound