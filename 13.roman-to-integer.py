#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        CHAR_MAP = {
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900,
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
                
        while i < len(s):
            if s[i:i+2] in CHAR_MAP:
                res += CHAR_MAP[s[i:i+2]]
                i += 2
            elif s[i] in CHAR_MAP:
                res +=  CHAR_MAP[s[i]]
                i += 1
        return res
