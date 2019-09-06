#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#
class Solution(object):
    # recursion
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        s_map = dict()
        
        def getWord(s):
        
            if s in wordDict:
                return True
            
            if s in s_map:
                return s_map[s]
            
            temp_s = ""
            for i in range(len(s)):
                temp_s += s[i]
                if temp_s in wordDict:
                    if s[i+1:] in s_map:
                        e = s_map
                    e = getWord(s[i+1:])
                    if e:
                        s_map[s] = True
                        return True
            s_map[s] = False
            return False
        return getWord(s)

