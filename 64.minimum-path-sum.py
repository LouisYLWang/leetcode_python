#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        dim_x = len(grid)
        dim_y = len(grid[0])
        for i in range(dim_x):
            for j in range(dim_y):
                if i and j:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i:
                    grid[i][j] += grid[i-1][j]
                elif j:
                    grid[i][j] += grid[i][j-1]
        return grid[dim_x-1][dim_y-1]

