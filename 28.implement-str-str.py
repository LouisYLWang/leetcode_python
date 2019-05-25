#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        ndl_len = len(needle)
        hay_ix = 0

        if ndl_len == 0:
            return 0

        while hay_ix + ndl_len <= hay_len :
            if haystack[hay_ix: hay_ix + ndl_len] == needle:
                return hay_ix
            else:
                hay_ix += 1
        return -1 



        '''
        hay_ix = 0
        needle_ix = 0
        needle_len = len(needle)
        if needle_len == 0:
            return 0 
        elif len(haystack) == 0 or needle_len > len(haystack):
            return -1
        else:
            while hay_ix < len(haystack):
                if haystack[hay_ix] == needle[needle_ix]:
                    if haystack[hay_ix:hay_ix+needle_len] == needle:
                        print(haystack[hay_ix:hay_ix+needle_len])
                        print(needle)
                        return hay_ix
                else:
                    hay_ix +=1
            else:
                return -1          
        '''
