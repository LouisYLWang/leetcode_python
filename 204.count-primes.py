#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrimes = [True] * (n + 1) 
        isPrimes[0] = False
        if n:
            isPrimes[1] = False

        for i in range(2, n):
            if isPrimes[i] == True:
                for j in range(2, (n//i)+1):
                    isPrimes[i*j] = False

        return sum(isPrimes[:-1])
    #dummy method 2
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        isPrimes = [0, 0, 1] + [1, 0] * ((n-1)//2)
        isPrimes = isPrimes[:n]
        for i in range(2, n):
            if isPrimes[i] == 1:
                for j in range(2, (n-1)//i+1):
                    isPrimes[i*j] = 0
        return sum(isPrimes)

        
        

