#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        ini = root.val
        cur_str = str(ini)
        stack = [root]
        while stack:
            cur = stack.pop()
            cur_str += "->%i" %cur.val
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            if (not cur.left) and (not cur.right):
                res.append(cur_str)
                cur_str = str(ini)
        return res

        

