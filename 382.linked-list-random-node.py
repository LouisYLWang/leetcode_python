#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.count = 0
        cur = head 
        while cur:
            cur = cur.next
            self.count += 1

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        pick = random.randrange(self.count)
        cur = self.head
        while pick:
            pick -= 1
            cur = cur.next
            
        return cur.val
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

