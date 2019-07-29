#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0] + nums + [0]
        zero_pos = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                if i - zero_pos - 1 > max_len:
                    max_len = i - zero_pos - 1
                zero_pos = i
        return max_len

