#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
class Solution:
    def compress(self, chars: List[str]) -> int:
        char_count = 0
        i = j = 0
        if not chars:
            return 0
        cur_char = chars[0]
            
        while i < len(chars):
            #print(i, chars[i], cur_char, char_count)
            if i == len(chars)-1:
                char_count += 1
                
            if chars[i] != cur_char or i == len(chars)-1:
                chars[j] = cur_char 
                j += 1             
                if char_count> 1:
                    #print(str(char_count))
                    for di in str(char_count):
                        chars[j] = di
                        j += 1
                cur_char = chars[i] 
                char_count = 1
            else:
                char_count += 1
            i += 1
        return j
        

