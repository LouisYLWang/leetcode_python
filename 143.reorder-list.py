#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        pre = None
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        half_1 = head
        half_2 = slow.next
        
        slow.next = None
        pre = None
        node = half_2
        
        while node:
            #temp = node.next
            #node.next = pre
            #pre = node
            #node = temp
            node.next, pre, node = pre, node, node.next

        node = pre
    
        cur = head
        while cur and node:
            #temp1 = node.next
            #temp2 = cur.next
            #cur.next = node
            #node.next = temp2
            #cur = temp2
            #node = temp1
            temp = node.next
            cur.next, node.next = node, cur.next
            cur = node.next
            node = temp
        return head
        
      
# @lc code=end

