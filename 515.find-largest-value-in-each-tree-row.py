#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        res = list()
        if not root:
            return res
        
        queue = list()
        queue.append(root)
        count = 1
        # use max() should be a little faster, but anyway...
        lvMax = -float('inf')
        
        while queue:
            for i in range(count):
                cur = queue.pop(0)
                if cur.val > lvMax:
                    lvMax = cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(lvMax)
            lvMax = -float('inf')
            count = len(queue)
        return res   
# @lc code=end

