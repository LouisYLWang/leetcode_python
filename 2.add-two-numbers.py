#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_cur = l1
        l2_cur = l2
        flag = 0
        res = ListNode(0)
        res_cur = res

        while l1_cur is not None or l2_cur is not None:
            
            if l1_cur is None:
                l1_cur = ListNode(0) 
            if l2_cur is None: 
                l2_cur = ListNode(0)
                
            cur_sum = l1_cur.val + l2_cur.val + flag
            res_cur.val = cur_sum % 10
            flag = cur_sum // 10
            
            if l1_cur.next is not None or l2_cur.next is not None:
                res_cur.next = ListNode(0)
                res_cur = res_cur.next
                l1_cur = l1_cur.next
                l2_cur = l2_cur.next
            else:
                if flag:
                    res_cur.next = ListNode(flag)
                return res
        return res
