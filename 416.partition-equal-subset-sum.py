#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        
        half = sum(nums) // 2 
        count = 0
        
        res_map = [[0 for i in range(half)]]
        
        res_map[0][nums[0]-1] = 1
        
        for i in range(1,len(nums)):
            res_map.append([0 for i in range(half)])
            #print(nums[:i])
            for j in nums[:i]:
                res_map[1][j-1] = 1
            #print('start', res_map)
            
            for k in range(half):   
                if k >= nums[i-1]:
                    res_map[1][k] = res_map[0][k] or res_map[0][k - nums[i-1]]
            #print('end', res_map)
            res_map.pop(0)
                 
        return res_map[-1]
        
        
        