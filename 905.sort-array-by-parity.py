#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
        res_1 = list()
        res_2 = list()
        for num in A:
            if num %2:
                res_2.append(num)
            else:
                res_1.append(num)
        
        return res_1 + res_2
        '''
        # in-place
        i = 0
        for j in range(len(A)):
            if A[j] %2 == 0:
                A[j], A[i] = A[i], A[j]
                i += 1
        return A
        
# @lc code=end

