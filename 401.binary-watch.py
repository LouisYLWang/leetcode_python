#
# @lc app=leetcode id=401 lang=python
#
# [401] Binary Watch
#
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        cur = 10
        while n > cur:
            i += 1
            cur += 9 * i * 10 ** (i - 1)
        
        cur -= 9 * i * 10 ** (i - 1)
        num = (n - cur)//i 
        digit = (n - cur)% i 

        return int(str(10**(i-1) + num)[digit])

