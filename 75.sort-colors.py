#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_hash = {0:0, 1:0, 2:0}
        for i in nums:
            count_hash[i] += 1
        
        sorted =  [0] * count_hash[0] + [1] * count_hash[1] + [2] * count_hash[2]

        for i in range(len(nums)):
            nums[i] = sorted[i]

    def sortColors(self, nums: List[int]) -> None:
        for id in range(len(nums)):
            temp = nums[id]
            nums[id] = 2
            if temp < 2:
                nums[j] = 1
                j += 1
            if temp < 1:
                nums[i] = 0
                i += 1
            #print(i, j)

    
        

