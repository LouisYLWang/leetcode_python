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

# method #2 recursion without altering the orignal tree
class Solution(object):
    ans = 0
    def add_value(self, root, val):
        if root:
            cur_val = root.val + 10 * val
            if root.left:
                self.add_value(root.left, cur_val)
            if root.right:
                self.add_value(root.right, cur_val)
            if not root.right and not root.left:
                self.ans += cur_val

    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.add_value(root, 0)
        return self.ans
