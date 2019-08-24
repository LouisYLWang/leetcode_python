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

#
class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_sub(root):
            if not root:
                return [0,0]
            
            left = rob_sub(root.left)
            right = rob_sub(root.right)
            
            return [max(left) + max(right), root.val + left[0] + right[0]]
    
        return max(rob_sub(root))
    
    


# This method use recursion with memorization, but not performance well
'''class Solution:
    rob_map = dict()
    def rob(self, root: TreeNode) -> int:
        def cur_out(root):
            if root in self.rob_map:
                if 0 in self.rob_map[root]:
                    return self.rob_map[root][0]
            
            ans_i_i = 0
            ans_o_o = 0
            ans_i_o = 0
            ans_o_i = 0
            if root.left or root.right:
                if root.left:
                    ans_i_i += cur_in(root.left)
                    ans_o_o += cur_out(root.left) 
                    ans_i_o += cur_in(root.left)
                    ans_o_i += cur_out(root.left) 
                if root.right:
                    ans_i_i += cur_in(root.right)          
                    ans_o_o += cur_out(root.right) 
                    ans_o_i += cur_in(root.right)  
                    ans_i_o += cur_out(root.right) 
            ans = max(ans_i_i, ans_o_o, ans_o_i, ans_i_o)
            
            if root not in self.rob_map:
                self.rob_map[root] = dict()        
            
            self.rob_map[root][0] = ans
            return self.rob_map[root][0]

    
        def cur_in(root):
            if root in self.rob_map:
                if 1 in self.rob_map[root]:
                    return self.rob_map[root][1]
            
            ans = root.val
            if root.left or root.right:
                if root.left:
                    ans += cur_out(root.left)
                if root.right:
                    ans += cur_out(root.right)
            
            if root not in self.rob_map:
                self.rob_map[root] = dict()
            
            self.rob_map[root][1] = ans
            
            return ans 

        
        if root: 
            return max(cur_out(root), cur_in(root))
        return 0'''
    
        

