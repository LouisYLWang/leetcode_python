#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#
class Solution:
    # use stack for nested questions is a natural way of thinking
    # 
    def decodeString(self, s: str) -> str:
        stack = [[1,""]]
        i = 0
        count = ''
        while i < len(s):
            if s[i] in '1234567890':
                count += s[i]
            elif s[i] == "[":
                stack.append([int(count),""])
                count = ""
            elif s[i] == "]":
                cur = stack.pop()
                stack[-1][1] += cur[0] * cur[1]
            else:
                stack[-1][1] += s[i]
            i += 1
        return stack[0][1]


