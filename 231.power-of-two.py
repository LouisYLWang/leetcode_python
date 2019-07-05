#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        return not(n & (n-1))
    '''
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        return int(bin(n)[3:]) == 0 and int(bin(n)[2]) == 1
    '''

