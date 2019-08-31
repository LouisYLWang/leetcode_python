#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ns_hash = [0 for i in range(n+1)]
        i = 1
        while i**2 <= n:
            ns_hash[i**2] = 1
            i += 1

        for i in range(1,n+1):
            if ns_hash[i] != 1:
                j_min = float('inf')
                j = 1
                while j ** 2 <= i // 2:
                # the dummy version: while j ** 2 <= i:
                    count = ns_hash[j ** 2] + ns_hash[i - j ** 2]
                    if count < j_min:
                        j_min = count
                    j += 1
                ns_hash[i] = j_min
        return ns_hash[n] 

    def numSquares(self, n: int) -> int:
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0        
        for i in range(0, n+1):
            # transformation function:
            # test all possible square and leave only the smallest combination
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i+j*j], dp[i] + 1)

                j += 1
        return dp[-1]   