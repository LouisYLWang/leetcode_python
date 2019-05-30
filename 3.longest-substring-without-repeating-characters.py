#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cache = 0
        s_dic = {}
        j = 0
        while j < len(s):
            s[j]


                if i in s_dic:
                    cache = 1
                    s_dic = {}
                else:
                    cache += 1
                s_dic[i] = 1
                max_len = max(cache, max_len)
            j += 1
        return max_len



