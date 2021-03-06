#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # or just simply intervals.sort()
        intervals = sorted(intervals, key = lambda _:_[0])

        ans = []
        
        # usage of [-1] indexing
        for interv in intervals:
            if not ans or ans[-1][1] < interv[0]:
                ans.append(interv)
            elif interv[1] > ans[-1][1]:
                ans[-1][1] = interv[1]
                
        return ans

        # personal solution
        '''
        if intervals:
            ans = [intervals[0]]
            i = 1
            n = 0

            while i < len(intervals):
                if intervals[i][0] <= intervals[i-1][1]:
                    intervals[i][0] = intervals[i-1][0]
                    if intervals[i][1] <= intervals[i-1][1]:
                        intervals[i][1] = intervals[i-1][1]
                    ans[n] = intervals[i]
                else:
                    ans.append(intervals[i])
                    n += 1
                i += 1
            return ans
        '''        
