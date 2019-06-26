#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#
class Solution:
    def reverseBits(self, n):
        #n = int('0b'+ str(n),2)
        res = 0
        i = 0
        while i < 31:
            res ^= (n >> 1 << 1 ^ n)
            n = n >> 1
            res = res << 1
            i += 1
        if n:
            res ^= (n >> 1 << 1 ^ n)
        return res
     


