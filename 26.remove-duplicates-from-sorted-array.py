#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #num_sum = 0
        i = 0
        if len(nums) == 1:
            return len(nums)
        else:
            while i < len(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    nums.pop(i)
                    continue
                else:
                    i += 1

            #print(nums)
            return len(nums)
        

