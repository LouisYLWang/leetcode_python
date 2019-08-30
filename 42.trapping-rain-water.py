#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height):
        def l_r_trap(height):
            i = 0
            ans = 0
            while i < len(height) - 1:
                temp = 0
                j = i + 1
                loc_max = height[i]
                while height[j] < height[i]:
                    temp += height[i] - height[j] 
                    if j + 1 < len(height):
                        j += 1
                    else:
                        ans += r_l_trap(height[i:][::-1])
                        return ans

                ans += temp
                i = j

            return ans
        
        def r_l_trap(height):
            i = 0
            ans = 0
            while i < len(height) - 1:
                temp = 0
                j = i + 1
                loc_max = height[i]
                while height[j] < height[i]:
                    temp += height[i] - height[j] 
                    if j + 1 < len(height):
                        j += 1
                    else:
                        return ans

                ans += temp
                i = j

            return ans
        
        return l_r_trap(height)