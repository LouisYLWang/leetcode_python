#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # recurive solution using min and max value of subtree
    def isValidBST(self, root):
        if not root:
            return True

        lValid = rValid = None
        
        if root.left:
            lValid = self.isValidBST(root.left)
            if lValid and lValid[1] >= root.val:
                return False
            
        if root.right:
            rValid = self.isValidBST(root.right)
            if rValid and rValid[0] <= root.val:
                return False
        
        
        if lValid == False or rValid == False:
            return False
        
        # a trick only for python since anything other than None and False return as True
        return lValid[0] if lValid else root.val, rValid[1] if rValid else root.val
        

