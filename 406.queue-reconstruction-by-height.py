#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x:[-x[0],x[1]])
        ans = list()
        for i in people:
            ans.insert(i[1], i)
        return ans

