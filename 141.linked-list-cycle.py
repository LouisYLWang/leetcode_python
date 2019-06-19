#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        if cur:
            while cur.next:
                if cur.next.val == ".":
                    return True
                cur.val = "."
                cur = cur.next
                #print(cur.val)
                #print(cur.next.val)
        return False






        

