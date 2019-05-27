#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur_str = ""
        res = ""
        i = 0
        if len(strs) == 0:
            return res
        else:
            min_len = min(map(len, strs))
            while i < min_len:
                flag = 0
                cur_str = strs[0][i]
                for str_ in strs:
                    if str_[i] != cur_str:
                        return res
                    else:
                        flag += 1 
                i += 1
                if flag == len(strs):
                    res += cur_str
            return res
