#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head:
            fast = head
            slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow != fast:
                    continue
                else:
                    slow = head
                    while slow != fast:
                        slow = slow.next
                        fast = fast.next
                    return slow
        return None


