#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            fast, slow = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            prev = None
            cur = slow
            while cur.next:
                temp = cur.next
                cur.next = prev
                prev = cur 
                cur = temp
            cur.next = prev

            while cur:
                if head.val != cur.val:
                    return False 
                else:
                    head = head.next
                    cur = cur.next
        return True

#
'''
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            fast, slow = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
        
            def reverse(head):
                prev = None
                cur = head
                while cur.next:
                    temp = cur.next
                    cur.next = prev
                    prev = cur 
                    cur = temp
                cur.next = prev
                return cur

            head2 = reverse(slow)
            cur = head2

            while cur:
                if head.val != cur.val:
                    return False 
                else:
                    head = head.next
                    cur = cur.next
        return True
        
'''
        


