#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        if n == 2:
            return ["(())","()()"]
    
        res = ["(" + self.generateParenthesis(n-1)[0]+")", "(" + self.generateParenthesis(n-1)[-1]+")"]
        
        for i in self.generateParenthesis(n-1)[1:-1]:
            res.append("(" + i + ")")
            res.append(i + "()")
            res.append("()" + i)
            
        for i in range(1,n):
            res.append(self.generateParenthesis(i)[0] + self.generateParenthesis(n-i)[0])
        res.append(self.generateParenthesis(n-1)[-1] +"()")
        return res

        #"()(())()"
