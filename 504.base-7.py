#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        cur = num
        bits = "0123456"
        
        if num < 0:
            cur = -num
    
        while cur // 7:
            res = bits[cur % 7] + res
            cur //= 7
            
        if num < 0:
            return '-'+ bits[cur] + res
        else:
            return bits[cur] + res


