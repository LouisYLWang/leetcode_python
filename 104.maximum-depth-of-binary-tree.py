#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count = 1
        max_dep = 0
        def DFS(cur):
            nonlocal count
            nonlocal max_dep
                
            if (cur.left is not None) | (cur.right is not None):
                if cur.left:
                    DFS(cur.left)
                if cur.right:
                    DFS(cur.right)
                count += 1
                max_dep = max(count, max_dep)

        DFS(root)
        return max_dep




