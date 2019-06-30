#
# @lc app=leetcode id=205 lang=python
#
# [205] Isomorphic Strings
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def toInt(s):
            index = 0
            char_dict = {}
            s_ = ""
            for char in s:
                if char not in char_dict:
                    char_dict[char] = index
                    cur_index = index
                cur_index = char_dict[char]
                s_ += str(cur_index)
                index += 1
            return s_
        return toInt(s) == toInt(t)

