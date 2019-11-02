#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        if root:
            queue = list()
            queue.append(root)
            count = 1
            lv = 0
            cur_ls = list()
            while queue:
                for i in range(count):
                    cur = queue.pop(0)
                    if lv%2 == 0:
                        cur_ls.append(cur.val)
                    if lv%2 != 0:
                        cur_ls.insert(0, cur.val)
                    if cur.left: queue.append(cur.left)
                    if cur.right: queue.append(cur.right)
                count = len(queue)
                lv += 1
                res.append(cur_ls)
                cur_ls = list()
        return res

# @lc code=end

