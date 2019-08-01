#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    # DP
    def coinChange(self, coins: List[int], amount: int) -> int:
        subprob_ls = [float('inf')] * (amount + 1)
        subprob_ls[0] = 0
        for i in coins:
            if i <= amount:
                subprob_ls[i] = 1
                
        for i in range(amount + 1):
            for coin in coins:
                if i <= coin:
                    continue
                subprob_ls[i] = min(subprob_ls[i], subprob_ls[i - coin] + 1)
        ans = subprob_ls[amount] 
        return ans if ans != float('inf') else -1

    # memotization can get correct result but O(kn), 
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def getMinCoin(coins, amount):
            if amount == 0:
                return 0
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
                return min_num if min_num != float('inf') else -1
        return getMinCoin(coins, amount)
    '''

