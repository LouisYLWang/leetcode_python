#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        s_len = len(s)
        res = 0
        for i in range(s_len):
            res += (ord(s[i]) - ord("A") +1) * (26 ** (s_len - i - 1))
            i += 1
        return res


