#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        def Helper(root):
            nonlocal count
            cur_coin = root.val
            if root.left:
                cur_coin += Helper(root.left)
            if root.right:
                cur_coin += Helper(root.right)
            
            count += abs(cur_coin - 1)
            return cur_coin - 1

        Helper(root)
        return count
# @lc code=end

