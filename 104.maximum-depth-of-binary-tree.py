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
        #count = 0
        #max_dep = 1
        def DFS(cur):
            #nonlocal count
            #nonlocal max_dep

            if cur is not None:
                if (cur.left is None) & (cur.right is None):
                    return 1
                if (cur.left is not None) | (cur.right is not None):
                    return max(DFS(cur.left), DFS(cur.right)) + 1
            return 0

        if root is None:
            return 0
        

        return DFS(root)
        #return #count + 1




