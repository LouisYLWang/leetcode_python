#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        n = int('0b'+ str(n),2)
        while n:
            if n != n >> 1 << 1:
                res += 1
            n = n >> 1
        return res

