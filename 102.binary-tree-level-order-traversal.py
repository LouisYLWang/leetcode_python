#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = list()
        count = 0
        res = list()
        local_res = list()
        if root:
            queue.append(root)
            while queue:
                count = len(queue)
                while count:
                    cur = queue.pop(0)
                    local_res.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    count -= 1 
                res.append(local_res)
                local_res = list()
        return res



        

