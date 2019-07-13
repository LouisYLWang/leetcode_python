#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
class Solution(object):
    '''
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        bitmap = [0]*26
        for i in s:
            bitmap[ord(i)-ord('a')] += 1
        s_len = len(s)
        i = 0
        while i < s_len:
            if bitmap[ord(s[i])-ord('a')] == 1:
                return i 
            i += 1
        return -1
    '''
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = dict()
        for i in s:
            if i not in map:
                map[i] = 0
            map[i] += 1
        s_len = len(s)
        i = 0
        while i < s_len:
            if map[s[i]] == 1:
                return i 
            i += 1
        return -1
