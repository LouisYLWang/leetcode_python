#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# best solution
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.preoder(t) in self.preoder(s)
        
    def preoder(self, node):
        if not node:
            s = "X"
        else:
            s = str(node.val)
            s += self.preoder(node.left)
            s += self.preoder(node.right)
        return " %s " %s 
# slow solution
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        stack = list()
        stack.append(s)
        flag = False
        while stack:
            cur = stack.pop()
            if cur.val == t.val:
                flag |= self.Helper(cur, t)
            if cur.left: stack.append(cur.left) 
            if cur.right: stack.append(cur.right) 
        return flag
    
    def Helper(self, a, b):
        stack_1 = list()
        stack_2 = list()
        stack_1.append(a)
        stack_2.append(b)
        while stack_1 and stack_2:
            cur_1 = stack_1.pop()
            cur_2 = stack_2.pop()
            if cur_1.val != cur_2.val:
                return False
            if cur_1.left: stack_1.append(cur_1.left) 
            if cur_1.right: stack_1.append(cur_1.right) 
            if cur_2.left: stack_2.append(cur_2.left) 
            if cur_2.right: stack_2.append(cur_2.right) 
        return (len(stack_1) == 0) & (len(stack_2) == 0)
    
# @lc code=end

