#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#


class Solution(object):
    def moveZeroes(self, nums):
        zero = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1
    
    # for this question, my version rebuit the value of nonzero index every time.
    # and I probably use way too much if sentence, which would slow down the process

    #SELF IMPLEMENTED VERSION
    '''
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
    '''
