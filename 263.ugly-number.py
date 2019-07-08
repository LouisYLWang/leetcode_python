#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#
class Solution(object):
    def isUgly(self, num):
        if num:
            while num%2 == 0:
                num /=2
            while num%3 == 0:
                num /=3
            while num%5 == 0:
                num /=5
            if num == 1:
                return True
        return False


