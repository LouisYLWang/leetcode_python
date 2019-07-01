#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

class Solution(object):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    def rotate(self, nums, k):
        n = len(nums)
        if k > n:
            k = k - n
        def reverse(start, end, nums):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1 
        
        reverse(0, n-1, nums)
        reverse(0, k-1, nums)
        reverse(k, n-1, nums)
        pass
    

    #O(n) space
    '''
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k - n
        nums[:] = nums[-k:] + nums[:-k]
    '''

        