#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        node_index = dict()
        for i in range(len(inorder)):
            node_index[inorder[i]] = i
            
        def split(preorder, ix_l, ix_r):
            if ix_l < ix_r and preorder:
                rootval = preorder.pop(0)
                rootix = node_index[rootval]

                root = TreeNode(rootval)
                root.left = split(preorder, ix_l, rootix)
                root.right = split(preorder, rootix + 1, ix_r)

                return root
            
        return split(preorder, 0, len(inorder))
