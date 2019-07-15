#
# @lc app=leetcode id=401 lang=python
#
# [401] Binary Watch
#
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def get_bin(n, bits):

            if n == 0:
                return set([0])
            if n == 1:
                return set([1<<i for i in range(0,bits)] )
            if n == bits:
                return set([sum(get_bin(1, bits))])
            res = set()
            for i in range(1, n):
                for j in get_bin(i, bits):
                    for k in get_bin(n-i, bits):
                        if j|k != j and j|k != k:
                            res.add(j|k)
                        
                            
            return res - get_bin(n-1, bits)
        

        res = []
        hour = 0
        while hour < 5:
            minutes = num - hour
            for i in get_bin(hour ,4):
                for j in get_bin(minutes, 6):
                    if i < 12:
                        if 10 <= j < 60:
                            res.append("%i:%i" %(i,j))
                        if j < 10:
                            res.append("%i:0%i" %(i,j))
            hour += 1
        res.sort()
        return res
 


