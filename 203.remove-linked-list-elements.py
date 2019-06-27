#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:break
        cur = head 
        while cur:
            if cur.val == val:
                pre.next = cur = cur.next
            else:
                pre, cur = cur, cur.next
        return head
            
            

        

