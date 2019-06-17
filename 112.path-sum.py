#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        path_sum = list()
        def getPathSum(root):

            nonlocal path_sum 
            if root:
                if root.left or root.right:
                    if root.left:
                        root.left.val += root.val
                    if root.right:
                        root.right.val += root.val
                    getPathSum(root.right)
                    getPathSum(root.left)
                else:
                    path_sum.append(root.val)

        getPathSum(root)
        return sum in path_sum

