# given x and y 
# compute x/y with only addition subtraction and shifting operators 
# book hint:
#   relate (x-y)/y
# a brute force method is to iteratively subtract y from x 
# until the remaining number is less than y
# and a better approach is to do a little more work in each iteration           
# 
# 
# 
# #
def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        y_power >>= 1 
        power -= 1
    result += 1 << power 
    x -= y_power
    return result
