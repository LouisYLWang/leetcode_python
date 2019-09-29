#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    # top down dp, self solition exceed time limit
    '''
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = -1

        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i]+1):
                if i+j < len(nums) and nums[i] >= 0 and nums[i+j] < 0:
                    nums[i] *= -1

        return nums[0] < 0 
    '''
    
    # greedy: push the boundary left, iterate back and once reach boundary, reset the boundary line
    
    def canJump(self, nums: List[int]) -> bool:
        cur = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            
            # once reach, reset the bound
            if i + nums[i] >= cur:
                cur = i

        return cur == 0

