#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        cur = head

        # check the rest listnode is enough for one group
        for i in range(k):
            # check first then increment, or when k = n will not inverse
            if not cur:
                return head
            cur = cur.next
        node = head
        pre = None

        for i in range(k-1):
            # one line method to inverse
            node.next, pre, node  =  pre, node, node.next
            # basic linkedlist inverse
            #temp = node.next
            #node.next = pre
            #pre = node
            #node = temp
            
        node.next = pre
        head.next = self.reverseKGroup(cur, k)
        return node
        

        
# @lc code=end

