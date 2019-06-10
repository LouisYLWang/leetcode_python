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
        cur = root
        if cur is not None:
            if (cur.left is None) & (cur.right is None):
                return 1
            if (cur.left is not None) | (cur.right is not None):
                return max(self.maxDepth(cur.left), self.maxDepth(cur.right)) + 1
        else:
            return 0




