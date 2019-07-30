#
# @lc app=leetcode id=665 lang=python
#
# [665] Non-decreasing Array
#
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        i = 0
        
        while i < len(nums) -1:
            if nums[i] > nums[i + 1]:
                flag += 1
                if i + 2 < len(nums):
                    if nums[i+1] < nums[i-1]:
                        return False
            i += 1
        return flag <= 1

        

