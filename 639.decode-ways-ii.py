#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#

# @lc code=start
class Solution:
    # very not efficient
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            if s[i-1] == "*":
                dp[i] = dp[i-1] * 9
                if i > 1: 
                    if s[i-2] != "*":
                        if s[i-2] == "1":
                            dp[i] += dp[i-2] * 9 
                        if s[i-2] == "2":
                            dp[i] += dp[i-2] * 6   
                    else:
                        # can not be zero
                        dp[i] += dp[i-2] * (26 - 1 - 10) 

            else:
                if s[i-1] > "0":
                    dp[i] += dp[i-1]
                if i > 1:
                    if s[i-2] == "*":
                        if s[i-1] <= "6":
                            dp[i] += 2 * dp[i-2]
                        else:
                            dp[i] += dp[i-2]
                    elif s[i-2:i] <= "26" and s[i-2:i] >= "10":
                        dp[i] += dp[i-2]
            
        return dp[-1]%(10**9 + 7)
  
# @lc code=end

