#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [[1,""]]
        ans = ""
        i = 0
        while i < len(s):
            if s[i] in '1234567890':
                stack.append([int(s[i]),""])
                i += 1
            elif s[i] == "]":
                cur = stack.pop()
                stack[-1][1] += cur[0] * cur[1]
            else:
                stack[-1][1] += s[i]
            i += 1
        return stack[0][1]

