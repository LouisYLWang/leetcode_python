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

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        cur = headA
        while cur.next:
            cur.val = "(%s)" %str(cur.val)
            cur = cur.next
        
        cur = headB
        while cur.next:
            if type(cur.val) == str:
                if cur.val[0] == "(" and cur.val[-1] == ")":
                    return cur.val[1:-1]
            cur = cur.next
        

        
        

