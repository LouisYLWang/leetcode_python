#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
'''
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        cur = n
        cur_res = guess(cur)
        print(cur, cur_res, n + cur_res * cur, cur_res == 0)
        if cur_res != 0:
            return self.guessNumber(cur + (cur_res * (n - cur//2)))
        return cur 

'''
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        right = n
        left = 0
        
        while left <= right:
            mid = (right + left)//2 
            cur = guess(mid) 
            
            if cur == 0:
                return mid
            elif guess(mid) <0:
                right = mid - 1
            else:
                left = mid + 1  
        
