#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#
# This problem is not suitable for python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        target = "aeiouAEIOU"
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in target and s[j] in target:
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                i +=1
                j -=1
            else:
                if s[i] not in target:  
                    i +=1
                if s[j] not in target:
                    j -=1
        return s


