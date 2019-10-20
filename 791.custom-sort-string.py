#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        chr_hash = [-1] * 26
        for s in S:
            chr_hash[ord(s) - ord('a')] += 1
        
        temp = ""
        for t in T:
            i = ord(t) - ord('a')
            if chr_hash[i] >= 0:
                chr_hash[i] += 1
            else:
                temp += t
        
        res = "" 
        
        for s in S:
            n = chr_hash[ord(s) - ord('a')]
            while n > 0:
                res += s
                n -= 1
        return res + temp 
# @lc code=end

