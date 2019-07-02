#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive 
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            cache = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = cache
        return root
    
# iterative
    def invertTree(self, root):
        if root:
            cur = root 
            q  = [cur]
            while q:
                cur = q.pop()
                cache = cur.left
                cur.left = cur.right
                cur.right = cache

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            return root 
