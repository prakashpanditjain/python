"""
Day 10. Two digits. At this point the streak is quietly rewriting how you approach problems.

Today’s challenge keeps the single-pass, state-tracking flavor you just practiced, but shifts it to arrays and boundaries.

Problem: Best Time to Buy and Sell Stock

You’re given an array prices, where prices[i] is the price of a stock on day i.
You may choose one day to buy and a later day to sell.

Return the maximum profit you can achieve.
If no profit is possible, return 0.
prices = [7, 1, 5, 3, 6, 4]
Buy at 1, sell at 6 → profit = 5
output = 5

prices = [7, 6, 4, 3, 1]
Prices only go down → no profit

0

"""


def max_profit(prices: list[int]) -> int:
    # your code
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit


max_pro = max_profit([100,10, 2, 1, 5, 3, 6, 7, 9, 4])
print(max_pro)