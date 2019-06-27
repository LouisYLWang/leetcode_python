#
# @lc app=leetcode id=202 lang=python
#
# [202] Happy Number
#
class Solution(object):
    table_a = {0:0}
    table_b = set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n in self.table_b) or n == 2 or n == 3:
            return False
        
        res = 0
        for i in str(n):
            cur = int(i)
            if cur in self.table_a:
                res += self.table_a[cur]
            else:
                self.table_a[cur] = cur**2
                res += cur**2
        if res == 1:
            return True
        print(res)
        self.table_b.add(n)
        return self.isHappy(res)

        

