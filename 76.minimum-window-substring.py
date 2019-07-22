#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = dict([[i, 0] for i in t])
        for i in t: target[i] += 1
        
        window = dict([[i, 0] for i in t])
        res = ""
        left, right = 0, 0
        counter = 0
        i = 0
        min_len = -float('inf')

        while right < len(s):
            if window[s[right]] > 0:
                counter -= 1
            window[s[right]] -= 1
            right += 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = t[left:right]
                if window[s[left]] == 0:
                    counter -= 1
                window[s[left]] += 1
                left += 1
        return res 


