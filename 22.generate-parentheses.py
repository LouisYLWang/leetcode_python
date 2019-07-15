#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return [""]
        res = list()

        for i in range(0,n):
            for j in self.generateParenthesis(i):
                for k in self.generateParenthesis(n-i-1):
                    res.append("(" + j + ")" + k)
        return res



