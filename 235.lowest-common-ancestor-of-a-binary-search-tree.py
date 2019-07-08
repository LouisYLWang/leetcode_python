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
        #make sure p < q
        if p.val > q.val:
            p,q = q,p
        if not root:
            return root
        if p.val <= root.val and q.val >= root.val:
            return root
        elif q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        else:
            return self.lowestCommonAncestor(root.right, p,q)


