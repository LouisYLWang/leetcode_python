#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if not obstacleGrid[0]:
            return 1
        
        hash = dict()
        ni = len(obstacleGrid)
        nj = len(obstacleGrid[0])
        
        def Helper(i, j):
            if (i,j) in hash:
                return hash[(i,j)]
            else:
                if i < ni and j < nj:
                    if obstacleGrid[i][j] == 1:
                        return 0
                    if i == ni -1 and  j == nj -1:
                        return 1

                    down = Helper(i+1, j) if j < nj else 0
                    right = Helper(i, j+1) if j < nj else 0
                    hash[(i,j)] = down + right
                    return down + right
                return 0
        return Helper(0, 0)
        
# @lc code=end

