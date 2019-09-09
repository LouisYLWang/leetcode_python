#
# @lc app=leetcode id=443 lang=python
#
# [443] String Compression
#
class Solution(object):
    def compress(self, chars):
        char_count = 1
        i = j = 0
        if not chars:
            return 0
        chars.append(None)
            
        while i < len(chars)-1:
            if chars[i] != chars[i+1]:
                chars[j] = chars[i]
                j += 1             
                if char_count> 1:
                    for di in str(char_count):
                        chars[j] = di
                        j += 1
                char_count = 1
            else:
                char_count += 1
            i += 1
        return j
        

