#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        res = 0

        for i in s[::-1]:
            if i != " ":
                res += 1
            if i == " " and res != 0:
                break
        return res 

