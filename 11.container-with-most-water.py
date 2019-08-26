#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i_l = 0 
        i_r = len(height) - 1
        max_a = min(height[i_r], height[i_l])
        
        while i_l < len(height) and i_r >= 0:
            
            r = height[i_r]
            l = height[i_l]
            
            cur_h = min(r, l)
            cur_a = (i_r - i_l) * cur_h
            
            if cur_a > max_a:
                max_a = cur_a
            
            if cur_h == l:
                i_l += 1
            else:
                i_r -= 1 
            
                
        return max_a

    # compact way
    def maxArea(self, height):
        max_a = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            cur_a = (r - l) * min(height[r], height[l])
            
            if cur_a > max_a:
                max_a = cur_a

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_a 

        

