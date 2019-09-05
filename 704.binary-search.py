#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            print(l,r,mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # notice mid should +- 1 to avoid infinate loop
                # since nums[mid] > target, should slack the boundary further right to avoid condition
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return -1
                 

