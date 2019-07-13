#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        bitmap = [0]*26
        for i in ransomNote:
            bitmap[ord(i)-ord('a')] +=1
        
        for i in magazine:
            if bitmap[ord(i)-ord('a')] > 0:
                bitmap[ord(i)-ord('a')] -= 1
        return sum(bitmap) == 0
    '''
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in ransomNote)
    '''
