#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ls_len = len(prices)
        profit_table = {}

        def getDiff(i_1, i_2):
            if (i_1, i_2) in profit_table:
                return profit_table[(i_1, i_2)]
            else:
                nonlocal max_profit
                res = 0

                if (i_2 - i_1) <= 1:
                    res = prices[i_2] - prices[i_1]

                else:
                    #mid = (i_1 + i_2) // 2
                    res = getDiff(i_1, i_2-1) + getDiff(i_2-1, i_2)
                profit_table[(i_1, i_2)] = res
                return res 

        if prices:
            for i in range(0, ls_len):
                getDiff(i,ls_len -1)
            print(profit_table)
            max_profit = max(profit_table.values())
            if max_profit > 0:
                return max_profit
        return 0

        

