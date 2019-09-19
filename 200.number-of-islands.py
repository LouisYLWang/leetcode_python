#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid or not grid[0]:
            return count
        nx = len(grid)
        ny = len(grid[0])

        def dfs(x, y):
            if grid[x][y] == '1':
                grid[x][y] = '0'
                if x+1 < nx and grid [x+1][y] == '1':
                    dfs(x + 1, y)
                if y+1 < ny and grid [x][y+1] == '1':
                    dfs(x, y + 1)
                if x-1 >= 0 and grid [x-1][y] == '1':
                    dfs(x-1, y)
                if y-1 >= 0 and grid [x][y-1] == '1':
                    dfs(x, y-1)
                    

        for i in range(nx):
            for j in range(ny):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
                    
        return count
