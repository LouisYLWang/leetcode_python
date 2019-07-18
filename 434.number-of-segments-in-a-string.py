#
# @lc app=leetcode id=434 lang=python
#
# [434] Number of Segments in a String
#
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        i = 0 
        if s:
            while i < len(s) - 1:
                if s[i] == " " and s[i+1] != " ":
                    res += 1
                i += 1
            if s[0] != " ":
                return res + 1
        return res 

