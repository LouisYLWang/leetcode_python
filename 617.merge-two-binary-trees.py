#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        stack_1 = [t1]
        stack_2 = [t2]
        zero_node = TreeNode(0)

        while stack_1 or stack_2:
            cur_1 = stack_1.pop()
            cur_2 = stack_2.pop()
            
            if cur_1 and cur_2:
                cur_1.val += cur_2.val
            else: continue
                
            
            if cur_2.left and not cur_1.left:
                cur_1.left = cur_2.left
            else:
                stack_2.append(cur_2.left)
                stack_1.append(cur_1.left)
            
            if cur_2.right and not cur_1.right:
                cur_1.right = cur_2.right
            else:
                stack_2.append(cur_2.right)
                stack_1.append(cur_1.right)    
            #print([i.val if i else None for i in stack_1], [i.val if i else None for i in stack_2])
                
        if not t1:
            return t2
        return t1 
                

            


