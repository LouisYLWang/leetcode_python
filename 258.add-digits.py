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
        sum = 0 
        for i in str(num):
            sum += int(i)
        if sum <= 9:
            return sum
        else:
            self.addDigits(sum)
