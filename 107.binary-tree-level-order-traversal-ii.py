#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:``
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            queue = [root]
            temp_len = 1
            while queue:
                temp_len = len(queue)
                res.insert(0, list(map(lambda x: x.val, queue)))
                while temp_len:
                    cur = queue.pop(0)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    temp_len -= 1
        return res

    