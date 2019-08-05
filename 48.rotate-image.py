#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix) - 1
        for i in range(dim):
            j = 0
            while j < dim - i:
                matrix[i][j], matrix[dim-j][dim-i] = matrix[dim-j][dim-i], matrix[i][j]
                j += 1
        
        m = 0
        while m < (dim + 1) //2:
            matrix[m], matrix[dim - m] = matrix[dim - m], matrix[m]
            m += 1

