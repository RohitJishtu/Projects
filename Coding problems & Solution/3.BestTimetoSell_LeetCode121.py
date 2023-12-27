# 121. Best Time to Buy and Sell Stock
# Easy
# 29.4K
# 1K
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

def BestDaytoSell(prices):
    # Initialize variables
    buy_price = prices[0]
    profit = 0
    best_profit_day = 0

    # Iterate through the prices array
    for i in range(len(prices)):
        # Skip the first day (index 0) as there's no previous day to compare
        if i == 0:
            pass
        else:
            # Check if selling on the current day would yield a higher profit
            if prices[i] - buy_price > profit:
                profit = prices[i] - buy_price
                best_profit_day = i + 1  # Record the best day to sell

            # Check if buying on the current day would be more profitable
            if buy_price - prices[i] > 0:
                buy_price = prices[i]  # Update the buying price

    return best_profit_day

prices = [7, 1, 5, 3, 6, 4]
print(BestDaytoSell(prices))
