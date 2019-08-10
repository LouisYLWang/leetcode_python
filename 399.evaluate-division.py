#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        div_map = dict()
        for [i,j], v in zip(equations, values):
            if i in div_map:
                div_map[i][j] = v
            else: div_map[i] = {j:v}
            if j in div_map:
                div_map[j][i] = 1/v
            else: div_map[j] = {i:1/v}
        
        print(div_map)

        def get_res(i, j, ans):

            if i not in div_map or j not in div_map:
                return -1.0
            elif i == j:
                return 1.0
            else:
                if j in div_map[i]:
                    return div_map[i][j]
                else:
                    for k in div_map[i]:
                        # use visited to control repeating visit
                        visited.add(i)
                        if k not in visited:
                            temp = get_res(k, j, ans)
                            # do not mistakenly use if temp 
                            if temp != -1:
                                return div_map[i][k] * temp
            # notice: if not find anything, remember to return -1
            return -1.0
                                
        # an alternative way of implementing get_res (more compact)
        def get_res(i, j, ans):
            if i not in div_map:
                return -1.0
            elif i == j:
                return 1.0
            
            for k in div_map[i]:
                if j == k:
                    return div_map[i][j]
                elif k not in visited:
                    visited.add(i)
                    temp = get_res(k, j, ans)
                    if temp != -1:
                        return div_map[i][k] * temp
            return -1.0
                        
        res =  list()
        for query in queries:
            visited = set()
            res.append(get_res(query[0], query[1], 1))
        return res
        
        



