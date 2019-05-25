#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ = x
        x_rev = 0 
        if x >= 0:
            x_rev = x_%10
            x_ = x_//10
            while x_ != 0:
                x_rev *= 10
                x_rev += x_%10
                x_ = x_//10
            return x_rev == x
        else:
            return False

