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

    # DP + binary search
    # important solution
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for num in nums]    
        lis = 0
        
        # iterate over nums, use num as target to make binary search, in order to find a suitable place to insert it into dp list
        for num in nums:
            l, r = 0, lis
            
            while l != r:
                m = (l + r) // 2
                if dp[m] < num:
                    l = m + 1
                else:
                    r = m
                    
            # between the range of 0 to lis, update or insert the current num to the position that is no smaller than num
            dp[l] = num
            print(dp)
            lis = max(l+1, lis)
        return lis


