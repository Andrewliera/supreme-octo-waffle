# write a program that takes an array denoting the daily stock, 
# and returns the maximum profit that could be made by buying and the selling tha stock
# ther is no need to buy if there is no profit
# book hint: focus only on valid differences 
# for this problem (as well as buy_sell_twice.py) the book has already developed a algorithm to solve this
# in an earlier section.
# 
# we could try to the simply calculate the difference of Min and Max  
# the issue with this is that the minimum value could after the maximum value
# which will miss the solution of the problem, where we have to buy before we sell.
# 
# brute force solution: we can use two nested loops, 
# by calculating every difference we see in an array as we iterate through it 
# comparing and updating, if Sell[i] - sell[j] > currentMaxProfit ->update the largest difference 
# since this solution has a complexity of O(n^2)
# the book mentions that using a divide-and-conquer algorithm would be good to get a better time complexity
# -> split Sell[] into two subarrays -> Sell[0, (2/n)] and Sell[((2/n) + 1), (n-1)]
#                                           ^                  ^ 
#                                        lower half         upper half
# 
# then, compute results in both sub arrays -> and combine 
# 
# 
# #


def buy_and_sell_stock_once(prices):
    current_min, max_profit = float('inf'), 0.0
    for price in prices: 
        max_profit_sell = price - current_min 
        max_profit = max(max_profit, max_profit_sell)
        current_min = min(current_min, price)
    return max_profit