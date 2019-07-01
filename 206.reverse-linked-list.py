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
        
        

