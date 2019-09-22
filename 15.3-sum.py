#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        if n < 3:
            return []
        
        nums.sort()
        res = set()
        
        for i, a in enumerate(nums[:-2]):
            # i >= 1 to make sure if all element equal to each other
            # a == nums[i-1] to jump over same element
            if i >= 1 and a == nums[i-1]:
                continue
            visited = set()
            for b in nums[i+1:]:
                if b not in visited:
                    # if -a-b appear again, get one result
                    visited.add(-a-b)
                else:
                    res.add((a, b, -a-b))
        return res
        

