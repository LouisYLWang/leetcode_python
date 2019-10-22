#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        num_hash = dict()
        num_hash_2 = [[] for i in range(9)]
        
        
        for i in range(n):
            for j in range(n):
                cur = board[i][j]
                
                if cur != ".":
                    cur_index = (i//3 * 3) + j//3
                    if cur in num_hash_2[cur_index]:
                        return False
                    num_hash_2[cur_index].append(cur)
                
                    if cur not in num_hash:
                        num_hash[cur] = [[],[]]
                    if i not in num_hash[cur][0]:
                        num_hash[cur][0].append(i)
                    else:
                        return False
                    if j not in num_hash[cur][1]:
                        num_hash[cur][1].append(j)
                    else:
                        return False

        return True
# @lc code=end

