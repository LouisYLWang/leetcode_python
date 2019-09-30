#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#
class Solution(object):

    # did not come up with own solution
    # DP 
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        if matrix:
            m = len(matrix)
            n = len(matrix[0])

            size = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    cur = int(matrix[i][j])
                    if not cur or not i or not j:
                        size[i][j] = cur
                        ans = max(ans, size[i][j])
                    else:
                        size[i][j] = min(size[i-1][j], size[i-1][j-1], size[i][j-1]) + 1
                        ans = max(ans, size[i][j])
                    
        return ans **2 
