#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    count = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def getPath(node):
            sum_ = [node.val]
            if node.val == sum:
                self.count += 1

            if node.left:
                sum_l = getPath(node.left)
                for s in sum_l:
                    sum_.append(node.val+s)
                    if node.val+s == sum:
                        self.count += 1
            if node.right:
                sum_r = getPath(node.right)
                for s in sum_r:
                    sum_.append(node.val+s)
                    if node.val+s == sum:
                        self.count += 1
            #print(node.val, sum_)
            return sum_
        if root:
            getPath(root)
            return self.count
        return 0
437

