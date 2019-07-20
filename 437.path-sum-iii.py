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
            path_, sum_, res_ = list(), list(), list()
            path_, sum_ = [[node.val]], [node.val]
            if node.val == sum:
                res_.append([node.val])

            if node.left:
                path_l, sum_l, res_l = getPath(node.left)
                res_ += res_l
                for p, s in zip(path_l, sum_l):
                    path_.append([node.val]+p)
                    sum_.append(node.val+s)
                    if node.val+s == sum:
                        res_.append([node.val]+p)
            if node.right:
                path_r, sum_r, res_r = getPath(node.right)
                res_ += res_r
                for p, s in zip(path_r, sum_r):
                    path_.append([node.val]+p)
                    sum_.append(node.val+s)
                    if node.val+s == sum:
                        res_.append([node.val]+p)

            return path_, sum_, res_
        if root:
            return len(getPath(root)[2])
        return 0


