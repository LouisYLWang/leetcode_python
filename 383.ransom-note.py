#
# @lc app=leetcode id=383 lang=python
#
# [383] Ransom Note
#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in ransomNote)

