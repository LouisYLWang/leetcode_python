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
        i = 0
        while right < len(s):
            if s[right] in target:
                window[i] += 1
                left, right = i, i
                right += 1


                while target != window:
                    left += 1
                res = t[left:right]
        return res 


