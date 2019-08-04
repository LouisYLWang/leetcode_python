#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]
        seq = list()
        
        if root:
            while stack:
                cur = stack.pop()
                seq.append(cur)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)

            for i in range(len(seq)-1):
                seq[i].right = seq[i + 1]
                seq[i].left = None

