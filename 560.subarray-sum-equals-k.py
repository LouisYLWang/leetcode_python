#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#
class Solution:

    # DP
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_map = {0:1}
        ans = 0
        sum_ = 0
        for n in nums:
            sum_ += n 
            # use iterative sum to control sum_ - k must be larger index - smaller index
            ans += sum_map.get(sum_ - k , 0)
            sum_map[sum_] = sum_map.get(sum_, 0) + 1
            
        return ans

    # nested 2nd fold for-loop: exceed time limit
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ls = [0 for i in nums]
        for i in range(len(nums)):
            sum_ls[i] = sum_ls[i-1] + nums[i]
        sum_ls = [0] + sum_ls
        ans = 0
        for r in range(len(sum_ls)):
            for l in range(r):
                if sum_ls[r] - sum_ls[l] == k:
                    ans +=1
        return ans
    

