#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# standard two-pointer solution
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        ans = 0 
        while l < r:
            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    ans += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    ans += r_max - height[r]
                r -= 1
        return ans
                
class Solution:
    def trap(self, height):
        def l_r_trap(height):
            i = 0
            ans = 0
            while i < len(height) - 1:
                temp = 0
                j = i + 1
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