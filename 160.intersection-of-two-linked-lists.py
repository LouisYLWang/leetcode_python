#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        cur_a = headA
        cur_b = headB
        while cur_a != cur_b:
            if cur_a:
                cur_a = cur_a.next 
            else:
                cur_a = headB
                
            if cur_b:
                cur_b = cur_b.next
            else:
                cur_b = headA
        return cur_a
        

