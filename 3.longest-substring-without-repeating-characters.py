#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        max_len = 0
        cache = 0
        for i in s:
            if cache ^ ord(i) > cache:
                cache ^= ord(i)
                counter += 1

            else:
                max_len = max(counter, max_len)
        return max_len



