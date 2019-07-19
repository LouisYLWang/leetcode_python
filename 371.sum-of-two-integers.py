#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#
class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        MASK = 0x100000000     
        c = a ^ b % MASK
        d = a & b % MASK
        if d!= 0:
            d <<= 1
            return self.getSum(c, d)
        else:
            if ~c <= MASK//2 and c <= MASK//2:
                return c
            return c ^ -MASK



