#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        loc_max = 0
        i = 0
        ans = 0
        while i < len(height):
            temp = 0
            j = i
            while height[j] < height[i] and j < len(height):
                temp += height[i] - height[j] 
                j += 1
            i = j 
            ans += temp
            i += 1
        return ans
