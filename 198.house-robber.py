#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
#recursion method
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        def subproblem(n):
            if n < 3:
                return max(nums[0:n])
            if n in cache:
                return cache[n]
            cur_res = max(subproblem(n-1), subproblem(n-2) + nums[n-1])
            cache[n] = cur_res
            return cur_res
        if nums:
            return subproblem(len(nums))
        return 0

        

