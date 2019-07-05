#
# @lc app=leetcode id=258 lang=python
#
# [258] Add Digits
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 9:
            return num 
        for i in range(1,10):
            if (num - i)%9 == 0:
                return i
