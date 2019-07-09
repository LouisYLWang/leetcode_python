#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        res = 0
        nums = len(prices)
        while j < nums:
            if prices[j] > prices[i]:
                res += prices[j] - prices[i]
            i += 1
            j += 1
        return res

        

