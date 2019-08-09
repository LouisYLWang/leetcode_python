#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans_map = [0 for i in range(len(T))]
        
        i = len(T) - 2
        while i >= 0:
            j = i+1
            # beware of the equal condition: if two consequential same temperature should not regard as 'a warmer temperature'
            if T[i] >= T[j]:
                while T[i] >= T[j] and ans_map[j]:
                    #print(i,j)
                    j += ans_map[j]
                if not ans_map[j]:
                    ans_map[i] = 0
                if T[i] < T[j]:
                    ans_map[i] = j - i
            else:
                ans_map[i] = 1
            i -= 1
        
        return ans_map
        

