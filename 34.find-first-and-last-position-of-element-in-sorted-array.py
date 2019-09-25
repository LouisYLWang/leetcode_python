#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        l = 0
        r = n - 1
        res = [-1, -1]
        while l < r:
            
            # at last, m == l, let left bound equal to target
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        if nums[r] != target:
            return res
        res[0] = r
        
        l = 0
        r = n - 1
        
        while l < r:
            
            # at last, m == r,  let right bound equal to target
            m = (l + r) // 2 + 1
            if target < nums[m]:
                r = m - 1
            else:
                l = m
        res[1] = l
                
        return res


