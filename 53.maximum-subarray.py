#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_sum = 0
        for num in nums:
            if cur_sum >= 0:
                cur_sum += num
            else:
                cur_sum = num
            cur_max = max(cur_max, cur_sum)
        return cur_max 

 