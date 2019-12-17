#
# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root:
            return []
        def getHeight(root):
            if not root:
                return 0, 0
            return (1 + max(getHeight(root.left)[0], getHeight(root.right)[0]) * 2,
                    1 + max(getHeight(root.left)[1], getHeight(root.right)[1]))
        
        m, n = getHeight(root)
        ret = [["" for i in range(m)] for i in range(n)]
        cur = (root, m//2)
        queue = [cur]
        lv = 0
        count = len(queue)
        while queue:
            for i in range(count):
                cur, pos = queue.pop(0)
                ret[lv][pos] = str(cur.val)
                if cur.left:
                    queue.append((cur.left, pos - 2**(n - 2- lv)))
                if cur.right:
                    queue.append((cur.right, pos + 2**(n - 2- lv)))
            count = len(queue)
            lv += 1
        return ret
# @lc code=end

