#
# @lc app=leetcode id=459 lang=python
#
# [459] Repeated Substring Pattern
#

class Solution:
    # slicky method
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1: -1]

    # slow but orthodox
    def repeatedSubstringPattern(self, s: str) -> bool:
        len_ = len(s)
        i = 0
        for t in range(1, len_//2 + 1):
            if len_ % t:
                continue
            i = t
            while i < len_ and s[i%t] == s[i]:
                i += 1
            if i == len_:
                return True
        return False
