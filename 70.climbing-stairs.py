#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        sol_map = dict()
        def get_res(n: int) -> int:
            nonlocal sol_map
            if n == 1:
                sol_map[1] = 1
                return 1
            if n == 2:
                sol_map[1] = 1
                return 2
            if n not in sol_map:
                sol_map[n] =  get_res(n - 1) + get_res(n - 2)
            return sol_map[n]

        return get_res(n)

