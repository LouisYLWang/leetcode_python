#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        bra_map = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        global chars
        global slen
        slen = len(s)
        chars = 0
        def print_bar():
            global chars
            global slen    
            if chars < slen:            
                input = s[chars]
                chars += 1
                if input in bra_map:
                    return input + str(print_bar()) + bra_map[input] + str(print_bar())
                else:
                    return ""
        if s == "":
            return True
        else:
            return (print_bar()[:-4] == s)

