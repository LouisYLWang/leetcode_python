#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            profit = p - min_price
            max_profit = max(profit, max_profit)
        return max_profit

