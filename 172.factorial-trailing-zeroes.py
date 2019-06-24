#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        cur = n // 5
        while cur:
            res += cur
            cur = cur // 5
            
        return res
