#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet =  'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower()
        
        while len(s)>1 :
            while s and s[0] not in alphabet:
                s = s[1:]

            while s and s[-1] not in alphabet:
                s = s[:-1]
            if s:
                if s[0] == s[-1]:
                    s = s[1:-1]
                else:return False

        return True
'''    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet =  'abcdefghijklmnopqrstuvwxyz0123456789'
        s = s.lower() 
        s_rev = ""     
        while s != s_rev :
            while s and s[0] not in alphabet:
                s = s[1:]
            while s and s[-1] not in alphabet:
                s = s[:-1]
            if s:
                s_rev += s[-1] 
                s = s[:-1]


            #if s:
            #    if s[0] == s[-1]:
            #        s = s[1:-1]
            #    else:return False

        return s == s_rev
'''



