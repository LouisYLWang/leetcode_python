#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def Helper(root):
            nonlocal res
            if root:
                res.append(root.val)
                for node in root.children:
                    Helper(node)

        res = list()
        Helper(root)
        return res
    # 
    def preorder(self, root: 'Node') -> List[int]:
        stack = list() #collections.deque()
        if root:
            stack.append(root)
        res = list()
        while stack:
            cur = stack.pop(0)
            res.append(cur.val)
            stack = cur.children + stack 
        return res
        

        
    # @lc code=end

