#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        fast = head
        slow = head
        pre = slow
        while fast and fast.next:
            fast = fast.next.next
            pre = slow 
            slow = slow.next
        
        pre.next = None
        
        left = self.sortList(head)    
        right = self.sortList(slow)
        
        if left.val > right.val:
            cur_h = right
            right = right.next
        else:
            cur_h = left
            left = left.next
        
        cur = cur_h
        
        while left and right:
            if left.val > right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next
            
        if left:
            cur.next = left
        if right:
            cur.next = right
        
        return cur_h
        
