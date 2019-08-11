#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

class Solution(object):
    def numTrees(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
    
    self.r_map = dict()
    # recursion with memorization 
    r_map = dict()
    def numTrees(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
            
        if n in self.r_map:
            return self.r_map[n]
        else:
            ans = 0
            for i in range(0, n):            
                ans += self.numTrees(i) * self.numTrees(n - i - 1)
            self.r_map[n] = ans
            return ans
    
        
        
    

