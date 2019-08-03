#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 2:
            return [nums]
        
        for i in range(1,len(nums)):            
            lefts = self.permute([nums[i]]) 
            rights = self.permute(nums[:i] + nums[i+1:])
            for l in lefts:
                for r in rights:
                    if l+r not in ans:
                        ans.append(l+r)
                    if r+l not in ans:
                        ans.append(r+l)
        return ans
        
        

