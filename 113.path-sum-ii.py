#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# solution 2
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
                for p, s in zip(path_l, sum_l):
                    path_.append([node.val]+p)
                    sum_.append(node.val+s)
            if node.right:
                path_r, sum_r = getPath(node.right)
                for p, s in zip(path_r, sum_r):
                    path_.append([node.val]+p)
                    sum_.append(node.val+s)
            return path_, sum_
        
        res = []
        if root:
            paths, sums = getPath(root)
            i = 0
            while i < len(sums):
                if sums[i] == sum:
                    res.append(paths[i])
                i +=1
        return res
'''
# solution 1
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
            if not node.left and not node.right:
                path_, sum_ = [[node.val]], [node.val]
                if node.val == sum:
                    res_.append([node.val])
                return path_, sum_, res_
              
            if node.left:
                path_l, sum_l, res_l = getPath(node.left)
                for p, s in zip(path_l, sum_l):
                    path_.append([node.val]+p)
                    sum_.append(node.val+s)
                    if node.val+s == sum:
                        res_.append([node.val]+p)
            if node.right:
                path_r, sum_r, res_r = getPath(node.right)
                for p, s in zip(path_r, sum_r):
                    path_.append([node.val]+p)
                    sum_.append(node.val+s)
                    if node.val+s == sum:
                        res_.append([node.val]+p)

            return path_, sum_, res_
        if root:
            return getPath(root)[2]
        return []
'''


