#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell

        '''
        explaination:

        buy[i]  = max(rest[i-1]-price, buy[i-1]) 
        sell[i] = max(buy[i-1]+price, sell[i-1])
        rest[i] = max(sell[i-1], buy[i-1], rest[i-1])

        rest[i] = sell[i-1]
        '''
