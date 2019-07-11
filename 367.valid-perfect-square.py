#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1 if num%2 else 2 
        
        while i**2 <= num:
            if i**2 == num:
                return True
            i += 2
        return False

