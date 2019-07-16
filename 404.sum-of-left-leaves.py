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
        if root:
            stack = [root]
            while stack:
                cur = stack.pop()
                if cur.left:
                    stack.append(cur.left)
                    if not cur.left.left and not cur.left.right:
                        res += cur.left.val
                if cur.right:
                    stack.append(cur.right)
        return res 
                

