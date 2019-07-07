#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#
class Solution(object):
    '''
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ = []
        t_ = []
        for i in s:
            s_.append(ord(i) - ord("a"))
        for j in t:
            t_.append(ord(j) - ord("a"))
        s_.sort()
        t_.sort()
        return s_ == t_
    '''
    def isAnagram(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2

