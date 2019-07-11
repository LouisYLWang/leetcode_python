#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#
class Solution(object):
    #binary search
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num 
        
        if num == 1:
            return True
        
        while left < right-1:
            mid = (left + right)//2
            if mid ** 2 < num:
                left = mid 
            if mid ** 2 > num:
                right = mid
            if mid ** 2 == num:
                return True
        return False

    #self implemented
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
    


