#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
class Solution(object):
    #O(1) space
    def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k > n:
        k = k - n

    def reverse(start, end):
        nonlocal nums
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1 
    
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)

    #O(n) space
    
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
    

            