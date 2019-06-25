#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        count = 0
        a = ""
        for i in bin(int("0b"+ str(n),2) ^ 4294967295)[2:]:
            a += str(~int(i) + 2)
            res += 2 ** count * (~int(i) + 2)
            count += 1
        return res 
        
            
        

