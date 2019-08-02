#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        



    # not workable
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        i = 1
        start = None
            
        while i < len(nums):
            if start == None:
                if nums[i - 1] >= nums[i]:
                    start = i - 1 
                end = start
            else:
                while nums[i] < nums[start] - 1 and start > 0:
                    start -= 1

                if nums[i - 1] <= nums[i]:
                    end = min(end, i- 1)
                else:
                    end = i 
            i += 1
        if start == None:
            return 0
        return end - start + 1 
