#
# @lc app=leetcode id=482 lang=python
#
# [482] License Key Formatting
#
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        ls_S = S.upper().split('-')
        res = ''.join(ls_S)
        char_len = len(res)
        len_1 = char_len % K if char_len % K else K
        ans = res[0:len_1]
        i = len_1
        while i < char_len:
            ans += '-%s' %res[i:i+K]
            i += K
        return ans
      

