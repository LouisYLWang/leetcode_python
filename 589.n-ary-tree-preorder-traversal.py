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
        
    # @lc code=end

