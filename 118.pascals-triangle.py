#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]
        i = 0 
        while i < numRows - 1:
            cur_ls = [1]
            j = 0
            while j < i:
                cur_ls.append(res[i][j] + res[i][j+1])
                j += 1
            cur_ls.append(1)
            res.append(cur_ls)
            i +=1 
            
        return res
                

        

