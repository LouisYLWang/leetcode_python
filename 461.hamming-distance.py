#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        cache = x ^ y
        ans = 0
        while cache != 0:
            if cache & 1:
                ans += 1
            cache >>= 1
        return ans
