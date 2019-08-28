#
# @lc app=leetcode id=392 lang=python
#
# [392] Is Subsequence
#
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0 
        n_s = len(s)
        n_t = len(t)
        count = 0
        while i < n_s and j < n_t:

            if t[j] == s[i]: 
                count += 1  
                i += 1
            j += 1 

        return count == n_s

