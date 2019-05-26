#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_i = 0
        res = 0
        while cur_i < len(nums):
            res += nums[cur_i]
            if res < 0:
                res = 0
                cur_i += 1
            else:
                cur_i += 1
        return res 


