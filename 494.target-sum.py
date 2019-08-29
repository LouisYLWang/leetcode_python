#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#
class Solution:
    def __init__(self):
        self.res_hash = dict()
        
    def findTargetSumWays(self, nums, S):
        len_ = len(nums)
        if (len_, S) in self.res_hash:
            return self.res_hash[(len_, S)]
        count = 0
        if nums:
            if len(nums) == 1:
                if nums[0] == S: 
                    count += 1
                if nums[0] == -S:
                    count += 1
            else:                 
                count += self.findTargetSumWays(nums[:-1], S + nums[-1])
                count += self.findTargetSumWays(nums[:-1], S - nums[-1])
        self.res_hash[(len_, S)] = count 
        return count
        