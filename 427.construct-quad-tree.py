#
# @lc app=leetcode id=427 lang=python
#
# [427] Construct Quad Tree
#
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        gl = len(grid)
        isLeaf = True
        topLeft, topRight, bottomLeft, bottomRight = None, None, None, None
        if sum(map(sum, grid)) == sum(map(len, grid)):
            val = True
        elif sum(map(sum, grid)) == 0:
            val = False
        else:
            val = "*"
            isLeaf = False
            topLeft_g = list(map(lambda a: a[0:len(a)//2],grid[0:gl//2]))  
            topRight_g = list(map(lambda a: a[len(a)//2:],grid[0:gl//2])) 
            bottomLeft_g = list(map(lambda a: a[0:len(a)//2],grid[gl//2:]))  
            bottomRight_g = list(map(lambda a: a[len(a)//2:],grid[gl//2:])) 
            #print(topLeft)
            topLeft = self.construct(topLeft_g)
            topRight = self.construct(topRight_g)
            bottomLeft = self.construct(bottomLeft_g)
            bottomRight = self.construct(bottomRight_g)
            #print(self.construct(topLeft).val)
        cur = Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        return cur
        
        

