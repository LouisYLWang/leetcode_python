#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#
class Solution(object):
    count = 0
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        for i in range(len(s)):
            extendPalindrome(s, i, i)
            extendPalindrome(s, i, i + 1)
        return self.count

        def extendPalindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.count += 1
                l -= 1
                r += 1
