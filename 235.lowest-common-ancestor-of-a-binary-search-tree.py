#
# @lc app=leetcode id=235 lang=python
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            print(root.val)

            if root.left or root.right:
                cur_list = [root.val, root.left.val, root.right.val]
                if (p in cur_list) and (q in cur_list):
                    return root.val
                else:
                    if root.left:
                        self.lowestCommonAncestor(root.left, p, q)
                    if root.right:
                        self.lowestCommonAncestor(root.right, p, q)

            


