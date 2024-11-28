# 121. Best Time to Buy and Sell Stock
# Easy
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

Prices = [7,1,5,3,6,4]

def MaxProfit(Prices):
    maxprofit=0
    lastbuy=Prices[0]
    for toidayprice in Prices:
        print(toidayprice,lastbuy,maxprofit)
        tempprofit=0
        if toidayprice <= lastbuy:
            tempprofit=toidayprice-lastbuy
            lastbuy=toidayprice
        else:
            tempprofit=toidayprice-lastbuy
        maxprofit=max(tempprofit,maxprofit)
        # print(f'{toidayprice=},{lastbuy=},{maxprofit=}')

    return maxprofit
print(MaxProfit(Prices))


# Prompt for LLM:

# Based on the code provided above, please answer the following questions:

# Rate the code quality on a scale of 1 to 5 (1 being poor, 5 being flawless). 1 word answer
# Evaluate the problem-solving approach and provide a rating (1 to 5).1 word answer
# Analyze the time complexity (e.g., O(n)).1 word answer
# Analyze the space complexity (e.g., O(n)).1 word answer
# Identify the coder's strengths & coder's weaknesses in this code. 2 sentences 
