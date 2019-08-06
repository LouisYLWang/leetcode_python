#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = [1]
        i,j = 1,1
        # the first loop calculate the upper triangle:
        # [nums[0], nums[0] * nums[1], nums[0] * nums[1] * nums[2] ... nums[0] * ... * nums[n-2] * nums[n-1]]
        for num in nums[:-1]:
            i *= num
            ans.append(i) 

        # the second loop calculate the bottom triangle
        # [nums[n-1], nums[n-1] * nums[n-1], ... nums[n-1] * ... * nums[2] * nums[1], nums[n-1] ]
        for num in range(len(nums) - 1, 0, -1): 
            j *= nums[num]
            ans[num - 1] *= j
        return ans



