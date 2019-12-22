#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = list()
        self.backtrack(sorted(candidates), 0, [], target, res)
        return res
        
    def backtrack(self, nums, start, path, target, res):
        if target == 0:
            res.append(path)
            
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
                
            if nums[i] > target:
                break
            
            self.backtrack(nums, i + 1, path + [nums[i]], target - nums[i], res)
                
 # @lc code=end

