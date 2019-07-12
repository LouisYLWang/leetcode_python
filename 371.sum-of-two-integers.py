#
# @lc app=leetcode id=371 lang=python
#
# [371] Sum of Two Integers
#
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c = a ^ b
        d = a & b 
        if d!= 0:
            d << 1
            return self.getSum(c,d)
        else:
            return c
        '''
        cursor = 1
        sum_ = 0
        carry = 0
        while cursor != 0:
            a_ = a & cursor
            b_ = b & cursor
            cur_res = a_ ^ b_
            sum_ |= cur_res ^ carry
            carry = (a_ & b_) | cur_res & carry
            cursor <<= 1
            carry <<= 1
        return sum_
        '''




