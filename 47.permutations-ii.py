#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        visited = [0 for i in range(len(nums))]
        res = []
        self.dfs(sorted(nums), [], visited, res)
        return res
        
    def dfs(self, nums, path, visited, res):
        if len(path) == len(nums):
            res.append(path)
        for i in range(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[i-1] and nums[i] == nums[i - 1]:
                    continue
                visited[i]+=1
                self.dfs(nums, path + [nums[i]], visited, res)
                visited[i]-=1

    # @lc code=end

