#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res 
        
