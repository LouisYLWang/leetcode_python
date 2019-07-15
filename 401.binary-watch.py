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
                return [0]
            res = list()
            digit = n-1
            cur = 1 << digit
            while cur < 1 << bits:
                for i in get_bin(n-1, digit):
                    res.append(cur|i)
                digit += 1
                cur = 1 << digit
            return res
        
        res = []
        hour = 0
        while hour < 5 and hour <= num:
            minutes = num - hour            
            for i in get_bin(hour ,4):
                for j in get_bin(minutes, 6):
                    if i < 12 and j < 60:
                        res.append("%d:%.2d" %(i,j))
            hour += 1
        return res
        


