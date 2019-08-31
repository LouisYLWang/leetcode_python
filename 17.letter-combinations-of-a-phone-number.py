#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def get_two(i, j):                
            res = list()
            for i_ in i:
                for j_ in j:
                    res.append(i_+j_)
            return res
        
        def get_letters(n):
            if int(n) <= 9:
                n = int(n)
                if n == 7:
                    return 'pqrs'
                elif n == 8:
                    return 'tuv'
                elif n == 9:
                    return 'wyxz'
                else:
                    return [chr(i + ord('a')) for i in range(3 * n - 6, 3 * n - 3)]    
            else:
                cur = get_letters(int(n[0]))
                for i in range(1, len(n)):
                    cur = get_two(cur, get_letters(int(n[i]))) 
            return cur
        if digits:
            return get_letters(digits)
        return []    

