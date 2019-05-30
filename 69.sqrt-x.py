#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        cur_b = x // 2
        if x == 1:
            return x 

        while cur_b**2 > x:
            cur_b = cur_b //2
        else:
            if cur_b**2 == x:
                return cur_b
            if cur_b**2 < x:
                while not cur_b**2 > x:
                    cur_b += 1
                else:
                    cur_b -= 1
                    return cur_b

        