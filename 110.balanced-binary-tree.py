#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        result = True
        
        def getHeight(root):
            nonlocal result
            if not root:
                return 0
            
            l_h = getHeight(root.left)
            r_h = getHeight(root.right)

            if abs(l_h - r_h) > 1:
                result = False
            return 1 + max(l_h, r_h)

        getHeight(root)
        return result

