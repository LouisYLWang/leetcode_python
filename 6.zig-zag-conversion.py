#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    # double pointer
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        I = 1
        # flatuate between 0 ~ numRows-1
        J = 0

        if numRows == 1:
            return s
        
        res = ["" for i in range(numRows)]
        
        for i in range(n):
            # if touch boundary, reverse
            if J + I in [-1, numRows]:
                I *= - 1
            res[J] += s[i]
            J += I        
        return "".join(res)
        
    # self solution   
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        zag = 2 * numRows - 2
        if zag == 0:
            return s
        
        res = ["" for i in range(zag)]
        
        for i in range(n):
            key = i % (zag)
            if key < numRows:
                res[key] += s[i]
            
            else:
                res[zag - key] += s[i]
        
        return "".join(res)
       
        
# @lc code=end

