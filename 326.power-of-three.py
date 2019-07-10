#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 1
        
        while res <= n:
            if res == n:
                return True
            res *= 3
        return False

