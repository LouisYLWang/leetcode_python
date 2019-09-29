#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # slow but worked, straightforward 
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = [root] if root.val not in to_delete else list()
        stack = [root]
        # a small trick to boost the speed
        # to_delete = set(to_delete)

        while stack:
            cur = stack.pop()   
            if cur.val in to_delete:
                if cur.left and cur.left.val not in to_delete:
                    ans.append(cur.left)
                if cur.right and cur.right.val not in to_delete:
                    ans.append(cur.right)

            
            if cur.left:
                stack.append(cur.left)
                if cur.left.val in to_delete:
                    cur.left = None
                
            if cur.right:
                stack.append(cur.right)
                if cur.right.val in to_delete:
                    cur.right = None

        return ans
        

