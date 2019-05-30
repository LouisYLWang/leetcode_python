#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    # newton method:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return x 

        cur_a = x // 2
        while cur_a * cur_a > x:
            cur_a=(cur_a+(x//cur_a)) //2
        else:
            return cur_a

    '''
    dummy solution
    def mySqrt(self, x: int) -> int:
        cur_b = x // 2
        if x == 1:
            return x 

        while cur_b * cur_b > x:
            cur_b = cur_b //2
        else:
            if cur_b * cur_b == x:
                return cur_b
            if cur_b * cur_b < x:
                while not cur_b * cur_b > x:
                    cur_b += 1
                else:
                    cur_b -= 1
                    return cur_b
    '''

        