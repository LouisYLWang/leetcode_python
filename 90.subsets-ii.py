#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur = [temp + [nums[i]] for temp in cur]
            else:        
                cur = [temp + [nums[i]] for temp in res]
            res += cur
        return res
# @lc code=end

