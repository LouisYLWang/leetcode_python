#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # best answer "for me"
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = [(0, root)]
        res = []
        while stack:
            visited, node = stack.pop()
            if visited:
                res.append(node.val)
            else:
                if node.right:
                    stack.append((0, node.right))
                stack.append((1, node))
                if node.left:
                    stack.append((0, node.left))
        return res
    # or 
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(0,root)]
        ans = list()
        
        while stack:
            visited, node= stack.pop()
            if visited:
                ans.append(node.val)
            elif not node:
                continue
            else:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
        return ans
    
    # slower but compact method without visted label
    def inorderTraversal(self, root):
        stack = []
        ans = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
    

