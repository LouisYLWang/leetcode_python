#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(1, n):
            if int(s[i]) <= 9 and int(s[i]) > 0:
                dp[i+1] += dp[i]
            
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) >= 10:
                dp[i+1] += dp[i-1]

        return dp[-1]
# @lc code=end

