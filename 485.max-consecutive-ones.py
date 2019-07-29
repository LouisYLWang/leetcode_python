#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#
class Solution(object):
    # better method
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
    '''
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        cur_len = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_len += 1
            if nums[i] == 0:
                if cur_len > max_len:
                    max_len = cur_len
                cur_len = 0
        return max_len if cur_len < max_len else cur_len
    '''

