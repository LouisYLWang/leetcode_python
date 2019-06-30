#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#
#dummy method
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
                    #print(i,j)
        #print(isPrimes)
        return sum(isPrimes[:-1])

        
        

