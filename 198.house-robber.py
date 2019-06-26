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

#iteration method
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        cur_l = nums[0]  # n = 1
        cur_r = max(nums[0], nums[1]) # n = 2 

        for i in nums[2:]:
            cur_max = max(cur_l + i, cur_r)
            cur_l, cur_r =  cur_r, cur_max
        return cur_r
