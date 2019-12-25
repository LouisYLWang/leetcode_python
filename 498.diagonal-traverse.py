#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def helper(m, n, i, j, res, status):
            if i == m-1 and j == n-1:
                res.append(matrix[i][j]) 
                return res
            
            if i < m and j < n and i >= 0 and j >= 0:     
                res.append(matrix[i][j]) 
            # up
            if status == 0:
                if j == n - 1:
                    i += 1
                    status = 1
                elif i == 0:
                    j += 1
                    status = 1
                else:
                    i -= 1
                    j += 1
            # down
            else:
                if j == 0:
                    i += 1
                    status = 0
                elif i == m - 1:
                    j += 1
                    status = 0
                else:
                    i += 1
                    j -= 1   
            helper(m, n, i, j, res, status)
            
        res = list()
        if not matrix or not matrix[0]:
            return []
        helper(len(matrix), len(matrix[0]), 0, 0, res, 0)
        return res
                  
# @lc code=end

