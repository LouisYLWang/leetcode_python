#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #pmax = prices[-1] - prices[0] 
        pmax = 0
        curi = None
        
        if prices:
            if prices[-2] > prices[-1]:
                prices[:] = prices[:-1]

            for i in range(2, len(prices) -1):
                pcur = prices[i-1] - prices[i + 1]
                #print(i, pcur)
                if pcur > pmax:
                    pmax = pcur
                    curi = i
            pmax += prices[-1] - prices[0] 
            #print(prices, curi)
            if curi:
                #print('1half', prices[:curi])
                #print('2half', prices[curi+1:])
                #return self.maxProfit(prices[:curi]) + self.maxProfit(prices[curi+1:])
            return prices[-1] - prices[0]
        return 0