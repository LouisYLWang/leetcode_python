#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

class Solution(object):
    #best practice
    def countPrimes(self, n: int) -> int:
         if n < 3:
            return 0     
         else:
            # 首先生成了一个全部为1的列表
            output = [1] * n
            # 因为0和1不是质数,所以列表的前两个位置赋值为0
            output[0],output[1] = 0,0
             # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
             # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
            for i in range(2,int(n**0.5)+1): 
                if output[i] == 1:
                    output[i*i:n:i] = [0] * len(output[i*i:n:i])
         # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
         return sum(output)
                        
        
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

        
        

