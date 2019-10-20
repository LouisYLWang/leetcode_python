#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = list()
        stack.append(root)
        tar = root.val
        while stack:
            cur = stack.pop()
            if cur.val != tar:
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return True
        # @lc code=end

