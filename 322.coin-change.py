#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def getMinCoin(coins, amount):
            print(amount)
            if amount == 0:
                return 0
            if amount < 0 or amount < min(coins):
                return -1
            if amount in coins:
                return 1
            if amount in memo:
                return memo[amount]
            else:
                flag = False
                min_num = float("inf")
                for i in coins:
                    if i < amount:
                        cur = getMinCoin(coins, amount - i) 
                        if cur > 0:
                            if cur < min_num:
                                min_num = cur + 1
                                flag = True
                if flag:
                    memo[amount] = min_num
                    return min_num
                return -1   
        return getMinCoin(coins, amount)
        
        

