#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ""
        if digits == []:
            return []

        for i in digits:
            digits_str += str(i)
        
        res = []
        digits_int = int(digits_str) + 1
        for j in str(digits_int):
            res.append(int(j))
        return res

        '''
        def po(pos):
            if pos == 0:
                if po(pos+1) != 0:
                     digits.insert(pos, po(pos+1))
                return digits

            if pos == len(digits) -1 or po(pos+1):
                cache = digits[pos] + po(pos+1)
                if not cache // 10:
                    return 1
                else:
                    return 0
            else:
                return digits
        '''
