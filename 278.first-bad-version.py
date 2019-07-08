#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    # better 
    def firstBadVersion(self, n):
        if n:
            upper = n
            lower = 0
            while upper - lower > 1:
                mid = (upper + lower) // 2 
                if isBadVersion(mid):
                    upper = mid
                else: 
                    lower = mid
            return upper



    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n:
            upper = n
            lower = 0
            upper_pre = upper
            lower_pre = lower
            while upper - lower != 1:
                upper_pre = upper
                upper = (upper + lower) //2
                if not isBadVersion(upper):
                    upper = upper_pre
                    if not isBadVersion(lower):
                        lower_pre = lower
                        lower = (upper + lower) //2
                    else:
                        lower = lower_pre
            return upper
    
        

