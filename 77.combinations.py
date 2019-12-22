#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = list()
        nums = range(1, n+1)
        self.dfs(nums, k, 0, [], res)
        return res
    
    def dfs(self, nums, k, index, path, res):
        if k == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path + [nums[i]], res)
# @lc code=end

