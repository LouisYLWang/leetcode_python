#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    # slow non-workable solution
    # weird test case of -2147483648 /n -1
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2<<30 and divisor == -1:
            return 2147483647
        
        flag = (dividend <= 0) ^ (divisor <= 0)
        
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        if divisor > dividend:
            return 0
        
        res =  0
        cur = divisor
        n = 1
        while dividend - cur >= divisor:
            dividend -= cur
            cur = divisor
            n = 1
            while dividend >= cur:
                cur <<= 1 
                n <<= 1
            cur >>= 1
            res += (n >> 1)
            
        if flag:
            return -res - 1
        else:
            return res + 1
    
# @lc code=end

