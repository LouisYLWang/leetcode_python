#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        count = len(bin(num)[3:])
        if num == 1:
            return True
        if count%2:
            return False
        return int(bin(num)[2:]) == 10**count 

