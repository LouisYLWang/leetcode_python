#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    # memotization can get correct result but O(kn), 
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def getMinCoin(coins, amount):
            print(amount)
            if amount == 0:
                return 0
            #if amount < 0 or amount < min(coins):
            #    return -1
            if amount in coins:
                return 1
            if amount in memo:
                return memo[amount]
            else:
                min_num = float("inf")
                for coin in coins:
                    if amount < coin:
                        continue
                    cur = getMinCoin(coins, amount - coin) 
                    if cur == -1: continue
                    min_num = min(min_num, cur + 1)


                memo[amount] = min_num
                return min_num
        return getMinCoin(coins, amount)
        
        

