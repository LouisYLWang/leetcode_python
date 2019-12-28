#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1,n+1)
            
    def dfs(self, a, b): 
        if a == b:
            return [None]
        
        res = list()
        for i in range(a,b):
            left = self.dfs(a, i)
            right = self.dfs(i+1, b)
            for l in left:        
                for r in right:
                    head = TreeNode(i)
                    head.left = l
                    head.right = r
                    res.append(head)
        return res
# @lc code=end

