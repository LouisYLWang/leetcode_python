#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # recursion - slow
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:
            if head.next:
                newhead = head.next
                temp = head.next.next 
                head.next.next = head
                head.next = self.swapPairs(temp)
                return newhead
            else:
                return head
# @lc code=end

