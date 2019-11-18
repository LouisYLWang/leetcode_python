#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = list()
        while k:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
    # do not need to iterate through the whole tree
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = list()
        visited = list()
        sortls = list()
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur.val not in visited:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                visited.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
            elif cur.val in visited:
                sortls.append(cur.val)
        return sortls[k-1]
# @lc code=end

