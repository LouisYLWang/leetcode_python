#
# @lc app=leetcode id=290 lang=python
#
# [290] Word Pattern
#
# double hash is probably not the optimal method
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_hash = dict()
        str_hash = dict()
        i = 0
        pattern_len = len(pattern)
        str_ls = str.split()

        if pattern_len != len(str_ls):
            return False
        for i in range(0,pattern_len):
            if str_ls[i] not in pattern_hash:
                pattern_hash[str_ls[i]] = pattern[i]
            else:
                if pattern[i] != pattern_hash[str_ls[i]]:
                    return False
                
            if pattern[i] not in str_hash:
                str_hash[pattern[i]] = str_ls[i]
            else:
                if str_ls[i] != str_hash[pattern[i]]:
                    return False
        return True


        

