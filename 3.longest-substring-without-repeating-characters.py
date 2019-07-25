#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0 
        right = 0
        char_map = dict([i, 0] for i in s)
        longest = 0
        counter = 0
        while right < len(s):
            if char_map[s[right]] > 0:
                if counter > longest:
                    longest = counter
                if char_map[s[left]] > 0:
                    char_map[s[left]] -= 1
                left += 1
                counter -= 1

            else:
                char_map[s[right]] += 1
                right += 1
                counter += 1
        return max(longest, counter)
