#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

class Solution(object):
    bookeeper = dict()
    #self implemented
    def uniquePaths(self, m, n):
        
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1    
        if (m, n) in self.bookeeper:
            return self.bookeeper[(m, n)]
        elif (n, m) in self.bookeeper:
            return self.bookeeper[(n, m)]
        else:
            self.bookeeper[(n, m)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n -1)
            self.bookeeper[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n -1)
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n -1)
    '''
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        if (m, n) in self.bookeeper:
            return self.bookeeper[(m, n)]
        if (n, m) in self.bookeeper:
            return self.bookeeper[(n, m)]
        
        cur_res = 0
        
        for k in range(1, n + 1):
            cur_res += self.uniquePaths(m // 2, k) * self.uniquePaths(m - m // 2, n - k + 1)
        return cur_res
    '''        

