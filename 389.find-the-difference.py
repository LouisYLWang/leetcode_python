#
# @lc app=leetcode id=389 lang=python
#
# [389] Find the Difference
#
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = s+t
        res = 0
        for i in target:
            res ^= ord(i)
        return chr(res)

