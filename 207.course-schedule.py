#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#


class Solution(object):
    # bread first search
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for i in range(numCourses)]        
        
        g = dict()
        for (a, b) in prerequisites:
            indegree[b] += 1
            if a not in g:
                g[a] = list()
            g[a].append(b)
        
        q = list()        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        #print(indegree, g)
        count = 0
        while q:
            course = q.pop()
            count += 1
            if course in g and g[course]:
                for related in g[course]:
                    if indegree[related] != 0:
                        indegree[related] -= 1
                    if indegree[related] == 0:
                        q.append(related)
                        
        return count == numCourses
    # deep first search
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [0 for _ in range(numCourses)]
        # NEVER NEVER NEVER USE [[]] * n AGAIN!!!
        courses_map = [[] for _ in range(numCourses)]

        for course in prerequisites:
            courses_map[course[0]].append(course[1])

        def dfs(c):
            if visited[c] == 1:
                return False
            if visited[c] == 2:
                return True

            visited[c] +=1

            for course in courses_map[c]:
                if not dfs(course):
                    return False
            visited[c] +=1
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
