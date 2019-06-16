#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        cur = root
        if cur is not None:
            
            if (cur.left is None) & (cur.right is None):
                return 1
            elif (cur.left is not None) & (cur.right is not None):
                return min(self.minDepth(cur.left), self.minDepth(cur.right)) + 1
            else:
                return max(self.minDepth(cur.left), self.minDepth(cur.right)) + 1
            
        else:
            return 0

