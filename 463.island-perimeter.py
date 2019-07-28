#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#
class Solution(object):

    # standard method
    def islandPerimeter(self, grid):
        length = len(grid)
        width = len(grid[0])
        prm = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    if j == 0 or grid[i][j - 1] == 0:
                        prm += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        prm += 1
        return prm * 2

    
    # dummy O(2*m*n) method
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        plus, minus = 0, 0
        i, j = 0, 0
        side_len_1 = len(grid)
        side_len_2 = len(grid[0])
        while i < side_len_1:
            cache_1 = 0 
            j = 0 
            while j < side_len_2:
                if grid[i][j]:
                    plus += 1
                    if cache_1:
                        minus += 1
                    cache_1 = 1
                else:
                    cache_1 = 0
                
                j += 1
            i += 1
        i, j = 0, 0 
        while i < side_len_2:
            cache_2 = 0

            j = 0 
            while j < side_len_1:
                if grid[j][i]:
                    if cache_2:
                        minus += 1
                    cache_2 = 1
                else:
                    cache_2 = 0
                j += 1
            i += 1

        return 4 * plus - 2 * minus
    '''
        
        


