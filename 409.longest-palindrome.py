#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_count = dict()
        for i in s:
            if i not in s_count:
                s_count[i] = 0
            s_count[i] += 1
        
        res = 0
        hit = 0

        for i in s_count.values():
            if i >= 2:
                res += i//2*2
            hit += i%2
        if s and hit:
            res += 1
        return res

