#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)
        map_ = [0 for i in range(max_ - min_ + 1)]
        for i in nums:
            map_[i-min_] +=1
    
        i = len(map_) - 1
        while i:
            k -= map_[i]
            if k <= 0:
                return min_ + i
            i -= 1
        return min_ + i


