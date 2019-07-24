#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            if i < 0:
                i = -i
            if nums[i - 1] > 0:
                nums[i - 1] *= -1
            
        i = 0
        res = []
        while i < len(nums):
            if nums[i] > 0:
                res.append(i + 1)
            i += 1
        return res 

