#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
class Solution:
    # DP O(N^2) 
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums:
            n = len(nums)
            dp = [1 for num in nums]
            for i in range(n):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[j] + 1, dp[i])
            return max(dp)
        return 0

