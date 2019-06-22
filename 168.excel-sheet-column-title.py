#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#
class Solution(object):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = n - 1 
        local_i = n % 26
        if n // 26 != 0:
            return self.convertToTitle(n // 26) + (Solution.alphabet[local_i])
        return Solution.alphabet[local_i]
