#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    # self implemented
    '''
    def lengthOfLongestSubstring(self, s):
        left = 0 
        right = 0
        char_map = set()
        longest = 0
        counter = 0
        while right < len(s):
            if s[right] in char_map:
                if counter > longest:
                    longest = counter
                if s[left] in char_map:
                    char_map.remove(s[left])
                left += 1
                counter -= 1

            else:
                char_map.add(s[right])
                right += 1
                counter += 1
        return max(longest, counter)
    '''
    # better method O(n)
    def lengthOfLongestSubstring(self, s):
        res = 0 
        hash_ = dict()
        i = 0
        for j in range(len(s)):
            if s[j] in hash_:
                i = max(hash_[s[j]], i)
            res = max(res, j - i + 1)
            hash_[s[j]] = j + 1
        return res
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in window:
                window.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            window.add(s[i])
        return max_len
    '''
