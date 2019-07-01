#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# iterative method
class Solution:
    def reverseList(self, head):
        cur = head 
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head = pre 
        
        cur = head
        return head
        
# recursive method (slow)

class Solution:
    def reverseList(self, head):
        res = head
        def reverse(cur):
            nonlocal res
            if not cur:
                return res
            
            if cur.next:
                reverse(cur.next)
                cur.next.next = cur 
            else:
                res = cur        
            
            if cur == head:
                cur.next = None
                return res
        
        return reverse(head)


