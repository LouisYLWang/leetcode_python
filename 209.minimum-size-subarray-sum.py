#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    # sliding window
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cursum = 0
        l = float('inf')
        i = 0
        j = 0
        n = len(nums)
        
        while i < n:
            cursum += nums[i]
            while cursum >= s:
                l = min(i-j+1, l)
                cursum -= nums[j]
                j += 1
            
            i += 1
            
        return l if l != float('inf') else 0
# @lc code=end

