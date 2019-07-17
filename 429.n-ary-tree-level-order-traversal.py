#
# @lc app=leetcode id=429 lang=python
#
# [429] N-ary Tree Level Order Traversal
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        if root:
            queue = [root]
            temp_len = 1
            while queue:
                temp_len = len(queue)
                res.append(list(map(lambda x: x.val, queue)))
                while temp_len:
                    cur = queue.pop(0)
                    if cur.children:
                        queue += cur.children
                    temp_len -= 1
        return res

