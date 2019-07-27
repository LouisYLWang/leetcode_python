#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        temp = n + 1
        fast = head
        while temp:
            if not fast:
                head = head.next
                return head
            fast = fast.next
            temp -= 1
        slow = head
        if fast:
            while fast:
                fast = fast.next
                slow = slow.next
        slow.next = slow.next.next
        return head

