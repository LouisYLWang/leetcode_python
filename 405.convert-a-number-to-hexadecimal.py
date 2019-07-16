#
# @lc app=leetcode id=405 lang=python
#
# [405] Convert a Number to Hexadecimal
#
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num = 2**32 + num
        res = ''
        cur = num
        bits = "0123456789abcdef"
        while cur >> 4:
            res = bits[cur % 16] + res
            cur >>= 4
        return bits[cur] + res

