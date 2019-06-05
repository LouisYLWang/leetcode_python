#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left, right):
            if left and right:
                return (left.val == right.val) & isMirror(left.left, right.right) & isMirror(left.right, right.left)
            return left is right
        if not root:
            return True
        return isMirror(root.left, root.right)



'''
# dummy version
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            print(p.val,q.val)
            flag = p.val == q.val
            flag &= self.isSameTree(p.left, q.left)
            flag &= self.isSameTree(p.right, q.right)
            return flag
        return p is q

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def switch(cur):
            if cur:
                cur.left, cur.right = switch(cur.right), switch(cur.left)
            return cur

        if root.right and root.left:
            switch(root.right)
            return self.isSameTree(root.left, root.right)

        return root.left is root.right
'''
