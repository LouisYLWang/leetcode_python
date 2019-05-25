#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)
        start = 0
        res = ''
        positive = True

        if str_int[0] == "-":
            start = 1 
            positive = False
        for i in reversed(str_int[start:]):
            res += i
        if not positive:
            res = '-'+ res
        if -2147483648< int(res)<2147483647:
            return int(res)
        else:
            return 0



