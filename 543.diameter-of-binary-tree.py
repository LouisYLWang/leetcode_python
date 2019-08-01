#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_len = 0
        def DFS(root):
            nonlocal max_len

            if root:
                l_len = max(DFS(root.left)) + 1
                r_len = max(DFS(root.right)) + 1
                if l_len + r_len > max_len:
                    max_len = l_len + r_len
                return l_len, r_len
            return -1, -1

        DFS(root)
        return max_len

