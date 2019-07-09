#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0
        nonzero = 0
        numsize = len(nums)

        while zero < numsize and nonzero < numsize - 1:
            if nums[zero] == 0:
                nonzero = zero
                while nums[nonzero] == 0 and nonzero < numsize - 1:
                    nonzero += 1
                nums[zero], nums[nonzero] = nums[nonzero], nums[zero]                
            else:
                zero += 1
