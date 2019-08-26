#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        ans = 0
        while queue:
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
                cur.left.val += 10 * cur.val
            if cur.right:
                queue.append(cur.right)
                cur.right.val += 10 * cur.val
            if not cur.left and not cur.right:
                ans += cur.val
                
        return ans
