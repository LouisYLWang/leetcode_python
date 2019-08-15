#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def cur_out(root):
            ans = 0
            if root.left or root.right:
                if root.left:
                    ans += cur_in(root.left)
                if root.right:
                    ans += cur_in(root.right)
            return ans
    
        def cur_in(root):
            ans = root.val
            if root.left or root.right:
                if root.left:
                    ans += cur_out(root.left)
                if root.right:
                    ans += cur_out(root.right)
            return ans

        
        if root: 
            return max(cur_out(root), cur_in(root))
        return 0
    
    
        

