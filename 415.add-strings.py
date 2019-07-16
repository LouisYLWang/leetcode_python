#
# @lc app=leetcode id=415 lang=python
#
# [415] Add Strings
#
class Solution(object):
    # better
    def addStrings(self, num1, num2):
        res = ""
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        tar = ['0','1','2','3','4','5','6','7','8','9']

        while i >= 0 or j >= 0:
            cur_1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            cur_2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            res = tar[(carry + cur_1 + cur_2)% 10] + res 
            carry = (carry + cur_1 + cur_2) //10
            i -= 1
            j -= 1
        if carry:
            res  = tar[carry] + res
        return res

    '''    
    # dummy method
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res_1 = 0
        digit_1 = 1
        for i in num1[::-1]:
            res_1 += (ord(i) - ord('0')) * digit_1
            digit_1 *= 10

        res_2 = 0
        digit_2 = 1
        for i in num2[::-1]:
            res_2 += (ord(i) - ord('0')) * digit_2
            digit_2 *= 10
        tar = ['0','1','2','3','4','5','6','7','8','9']
        cur = res_1 + res_2
        res = ""
        while cur // 10:
            res = tar[cur % 10] + res
            cur //= 10
        res = tar[cur % 10] + res
        return res
    '''
