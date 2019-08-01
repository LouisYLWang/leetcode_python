#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def RDL_1(root, sum_):
            #print(root.val if root else None, mother.val if mother else None)
            if not root:
                return sum_
            
            sum_ = RDL_1(root.right, sum_)
            cur_val = root.val
            root.val += sum_
            sum_ += cur_val
            sum_ = RDL_1(root.left, sum_)
            return sum_
            
        RDL_1(root, 0)
        return root
    #self implemented
    def convertBST(self, root: TreeNode) -> TreeNode:
        def RDL_1(root, mother_val):
            if root:
                r_sum = RDL_1(root.right, mother_val)
                root.val += r_sum
                l_sum = RDL_1(root.left, root.val)
                return l_sum
            return mother_val
        RDL_1(root, 0)
        return root

    #This problem is not supposed to use LDR, but RDL (reverse inorder traversals )
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        def LDR_1(root):
            cur_ls = []
            if root:
                cur_ls = LDR_1(root.left)
                cur_ls.append(root.val)
                cur_ls += LDR_1(root.right)
            return cur_ls
        
        sorted_ls = LDR_1(root)
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                cur.val = sum(sorted_ls[sorted_ls.index(cur.val):]) 
                stack.append(cur.left)
                stack.append(cur.right)
        return root
    

