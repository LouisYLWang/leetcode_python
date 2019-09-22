#
# @lc app=leetcode id=621 lang=python
#
# [621] Task Scheduler
#
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        ct = Counter(tasks)
        count_ls = ct.values()
        count_ls.sort()
        
        max_ = max(count_ls)
        
        res = (n + 1) * (max_ -1)
        

        for i in ct:
            if ct[i] == max_:
                res += 1
        return max(res, len(tasks))
        

