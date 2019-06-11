#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        len_nums = len(nums)
        if len_nums > 1:
            i_mid = len_nums // 2
            root = TreeNode(nums[i_mid])
            root.left = self.sortedArrayToBST(nums[:i_mid])
            root.right = self.sortedArrayToBST(nums[i_mid + 1:])
            return root
        else:
            if len_nums:
                root = TreeNode(nums[0])
                return root
        

