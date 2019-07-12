#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = n//2
        cur_res = self.guessNumber(cur)
        if cur_res == 0:
            return cur
        else:
            return self.guessNumber((n + cur_res * cur) //2)

        
        

