#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a_len = len(a) 
        b_len = len(b)
        max_len = max(a_len, b_len)

        if not max_len:
            return ""

        if a_len < b_len:
            a = "0" * (b_len - a_len) + a
        if a_len > b_len:
            b = "0" * (a_len - b_len) + b

        res = ""
        
        def cal_digit(i):
            nonlocal max_len
            nonlocal res
            if i == max_len:
                return 0
            
            cur_a = int(a[i])
            cur_b = int(b[i])
            cur_res = cal_digit(i+1) + cur_a + cur_b
            res = str(cur_res%2) + res
            if i != 0:
                return cur_res//2
            elif cur_res//2:
                res = str(cur_res//2)  + res
                

        cal_digit(0)
        return res 

            


