#
# @lc app=leetcode id=520 lang=python
#
# [520] Detect Capital
#
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 1:
            def isUpper(s):
                return s.upper() == s

            ls = list(map(isUpper, word))

            if ls[1]:
                if not ls[0]:
                    return False
                flag = True
            else:
                flag = False

            for i in ls[1:]:
                if i != flag:
                    return False
        return True 

