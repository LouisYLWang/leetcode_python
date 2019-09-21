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
        res_map = [0 for i in range(half + 1)]
        res_map[0] = 1
        for num in nums:
            for i in range(half, 0, -1):
                if i >= num:
                    # when i == num, set res_map[num] to 1
                    # reverse iteration to make sure in one iteration, the smaller i result will not change the larger i result
                    res_map[i] = res_map[i] or res_map[i - num]
        return res_map[-1]
        
        
        
        