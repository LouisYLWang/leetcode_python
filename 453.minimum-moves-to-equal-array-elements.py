#
# @lc app=leetcode id=453 lang=python
#
# [453] Minimum Moves to Equal Array Elements
#
class Solution:
    def minMoves(self, nums):
        minvalue = min(nums)
        sum_ = sum(nums)
        n = len(nums)
        return sum_ - minvalue * n
        
        
        
