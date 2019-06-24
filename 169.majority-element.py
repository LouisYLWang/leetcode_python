#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
class Solution(object):
    # boyer - moore algorithm 
    def majorityElement(self, nums):
        flag = 0
        cur_mode = None
        for i in nums:
            if flag == 0:
                cur_mode = i
            if i == cur_mode:
                flag += 1
            else:
                flag -= 1
        return cur_mode

    # self implemented
    '''
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
    '''
    
