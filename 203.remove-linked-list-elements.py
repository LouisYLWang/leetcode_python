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
        cur = head 
        if cur.val == val:
            head = cur.next

        while cur.next.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                cur = cur.next
                
        if cur.next.val == val:
            cur.next = None
        
        return head
            
            

        

