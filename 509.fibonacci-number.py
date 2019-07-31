#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#
class Solution(object):
    # memorization 
    memo = dict()
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        if N in self.memo:
            return self.memo[N]
        else:
            self.memo[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.memo[N]

    # pure recursion
    '''
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N - 1) + self.fib(N-2)
    '''
