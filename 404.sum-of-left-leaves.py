#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        while root:
            if root.left:
                res += root.left.val
                self.sumOfLeftLeaves(root.left)
            if root.right:
                self.sumOfLeftLeaves(root.right)
            return res
