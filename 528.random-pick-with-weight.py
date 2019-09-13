#
# @lc app=leetcode id=528 lang=python
#
# [528] Random Pick with Weight
#
class Solution:

    def __init__(self, w: List[int]):
        self.count = sum(w)
        self.n = len(w)
        cur = 0
        self.sumls = [0]
        for a in w:
            cur += a
            self.sumls.append(cur)
        
        

    def pickIndex(self) -> int:
        target = random.randrange(self.count)
        l = 0 
        r = n - 1
        while l <= r:
            if target < w[l]:
                r = (r + l)//2 + 1
            elif target > w[r]:
                l = (r + l)//2 - 1

        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

