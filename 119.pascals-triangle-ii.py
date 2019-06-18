#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1]
        priorRow = self.getRow(rowIndex - 1)
        i = 0
        while i <= rowIndex - 2:
            res.append(priorRow[i] + priorRow[i+1])
            i += 1
        return res + [1]


            

        

