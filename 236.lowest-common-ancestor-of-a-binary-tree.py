#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            l = self.lowestCommonAncestor(root.left, p, q) 
            r = self.lowestCommonAncestor(root.right, p, q)
            
            if root == p or root == q:
                if l or r:
                    return root
            else:
                if l and r:
                    return root
                else:
                    return l or r
        return root
        

