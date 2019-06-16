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
        res = [[root.val]]
        def getSubls(root):
            #res.insert(0, [root.left.val, root.right.val])
            subs = list()
        

            if root:
                if root.left is not None:
                    subs.append(root.left.val)
                if root.right is not None:
                    subs.append(root.right.val)
        

            if subs:
                if getSubls(root.left) + getSubls(root.right):
                    res.insert(0, getSubls(root.left) + getSubls(root.right))  
                res.insert(0,subs)
                return subs

        print(root.val)
        getSubls(root)
        return res
    