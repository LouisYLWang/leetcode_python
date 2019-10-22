#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        cur = head
        if not cur or not cur.next: return cur
        len_ = 1
        while cur.next:
            cur = cur.next
            len_ += 1 
        
        if k%len_ == 0: return head

        n = 0
        cur = head
        while cur:
            if n == len_ - k%len_:
                new_head = cur
                pre.next = None
                cur = new_head
                while cur.next:
                    cur = cur.next
                cur.next = head
                return new_head

            pre = cur
            cur = cur.next
            n += 1

# @lc code=end

