#
# @lc app=leetcode id=1019 lang=python
#
# [1019] Next Greater Node In Linked List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head:
            cur = head
            count = 0
            res = list()
            while cur:
                if cur > cur.next:
                    count += 1
                    cur = cur.next
                else:
                    cur = cur.next
                    while count:
                        res.append(cur.val)
        return res
                        

