#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        stack = [root]
        sum_hash = dict()

        def getPath(node):
            path_, sum_ = [], []
            if not node.left and not node.right:
                path_, sum_ = [[node.val]], [node.val]
                return path_, sum_
              
            if node.left:
                path_l, sum_l = getPath(node.left)
                for path_, sum_ in zip(path_l, sum_l):
                    path_.append([node.val]+path_, node.val+sum_)
            if node.right:
                path_r, sum_r = getPath(node.right)
                for path_, sum_ in zip(path_r, sum_r):
                    path_.append([node.val]+path_, node.val+sum_)
            return path_, sum_

        print(getPath(root))


