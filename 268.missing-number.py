#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum_ = 0
        count = 0
        for i in nums:
            sum_ += i
            count += 1

        return int((1+count)*count/2) - sum_ 
        

