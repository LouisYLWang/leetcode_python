#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            flag = p.val == q.val
            flag &= self.isSameTree(p.left, q.left)
            flag &= self.isSameTree(p.right, q.right)
            return flag
        else:
            return p is None and q is None


