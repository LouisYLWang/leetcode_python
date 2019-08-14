#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return s
        
        else:
            def Palindrome(i, j):
                count = j - i - 1
                if s[i] != s[j]:
                    return i, j

                while i >= 0 and j < n:
                    if s[i] == s[j]:
                        i -= 1
                        j += 1
                        count += 2
                    else:
                        break
                return i+1, j

            n_max = 0
            res = None

            for i in range(n - 1):
                l, r = Palindrome(i, i)
                count_ = r - l 
                if count_ > n_max:
                    res = s[l:r]
                    n_max = count_

                l, r = Palindrome(i, i + 1)
                count_ = r - l 
                if count_ > n_max:
                    res = s[l:r]
                    n_max = count_
        return res
