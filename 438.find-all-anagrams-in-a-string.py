#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = list()
        temp = dict((i, 0) for i in p + s)
        target = temp.copy()
        letters = temp.copy()
        i , j = 0, len(p)
        
        for letter in p:
            target[letter] += 1
        for l in s[i:j]:
            letters[l]+= 1
        if letters == target:ans.append(i)

        while j < len(s):
            if s[j] in p:
                letters[s[i]] -= 1
                i += 1
                letters[s[j]] += 1
                j += 1

            else:
                i += len(p) + 1
                j = i + len(p)
                letters = temp.copy()
                for l in s[i:j]:
                    letters[l]+= 1  
            
            if letters == target:
                ans.append(i)
        return ans