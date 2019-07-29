#
# @lc app=leetcode id=501 lang=python
#
# [501] Find Mode in Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def LDR(root):
            if not root.left and not root.right:
                return [root.val]
            temp = []
            if root.left:
                temp.extend(LDR(root.left))
            temp.append(root.val)
            if root.right:
                temp.extend(LDR(root.right))
            return temp

            
        if not root:
            return []
        sort_ls = LDR(root)
        max_rep = 1
        count = 0
        pre = None
        ans = []
        for cur in sort_ls:
            if cur == pre:
                count += 1
            else: count = 1
            if count == max_rep:
                ans.append(cur)
            if count > max_rep:
                max_rep = count
                ans = [cur]
            pre = cur
        return ans
