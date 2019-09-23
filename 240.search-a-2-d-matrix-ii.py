#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            nx = len(matrix[0])
            ny = len(matrix)
            # initial setting, start from top right
            i = 0
            j = nx - 1

            while j >= 0 and i < ny:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    i += 1
                else:
                    j -= 1
        return False

