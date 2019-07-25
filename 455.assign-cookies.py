#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        cookie = 0
        while cookie < len(s) and g:
            if s[cookie] >= g[0]:
                ans += 1
                s.pop(0)
                g.pop(0)
                cookie -= 1
            cookie += 1
        return ans



