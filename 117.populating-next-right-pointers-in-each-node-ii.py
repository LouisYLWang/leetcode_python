#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            q = [root]
            count = 1
            pre = Node(0)
            while q:
                for i in range(count):
                    cur = q.pop(0)
                    pre.next = cur 
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                    pre = cur

                cur.next = None
                pre = Node(0)
                count = len(q)

            return root 
# @lc code=end

