#
# @lc app=leetcode id=822 lang=python3
#
# [822] Card Flipping Game
#

# @lc code=start
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        i = 0
        trash = set()
        res = 2001
        while i < len(fronts):
            if fronts[i] == backs[i]:
                trash.add(fronts[i])
            i += 1
        for num in fronts + backs:
            if num not in trash:
                res = min(res, num)
        return res if res != 2001 else 0 
       
        

# @lc code=end

