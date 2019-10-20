#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        zag = 2 * numRows - 2
        if zag == 0:
            return s
        
        res = [[] for i in range(zag)]
        
        for i in range(n):
            key = i % (zag)
            if key < numRows:
                res[key].append(s[i])
            
            else:
                res[zag - key].append(s[i])
        
        ans = ""
        for col in res:
            for chr in col:
                ans += chr

        return ans
        
# @lc code=end

