#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n_x = len(board)
        n_y = len(board[0])
        char_map = dict()
        for i in range(n_x):
            for j in range(n_y):
                if board[i][j] not in char_map:
                    char_map[board[i][j]] = [(i,j)]
                else: char_map[board[i][j]].append((i,j))
        print(char_map)
        
        def traverse(cord, i, visited):
            res = False
            if 0 <= cord[0] < n_x and 0 <= cord[1] < n_y:
                
                if cord and cord not in visited:
                    x = cord[0]
                    y = cord[1]
                    if i == len(word) - 1:
                        if board[x][y] == word[i]:
                            print(i,cord, board[x][y], word[i], board[x][y] == word[i])
                            #print(True)
                            return True 
                        else:
                            print(i,cord, board[x][y], word[i], board[x][y] == word[i])
                            #print(False)
                            return False
                    else:
                        print(i, cord, board[cord[0]][cord[1]],  word[i], board[x][y] == word[i])
                        if board[x][y] == word[i]:
                            visited.add((x,y))
                            print(visited)

                            u = (x - 1, y) #if x > 0 else None 
                            d = (x + 1, y) #if x < n_x -1 else None 
                            l = (x, y - 1) #if y > 0 else None 
                            r = (x, y + 1) #if x < n_y -1 else None 
                            
                            res |= traverse(u, i + 1, visited)
                            res |= traverse(d, i + 1, visited)
                            res |= traverse(l, i + 1, visited)
                            res |= traverse(r, i + 1, visited)
                            if not res:
                                visited.remove((x,y))
                                print(visited)
            return res 
        #return traverse((0,0), 0, set())
        ans =  False     
        if word[0] in char_map:
            for i in char_map[word[0]]:
                ans |= traverse(i, 0, set())
        return ans
 

