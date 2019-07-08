#
# @lc app=leetcode id=278 lang=python
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur_i = n//2
        while not isBadVersion(cur_i):
            cur_i //= 2
        print(cur_i)
        while isBadVersion(cur_i):
            cur_i += 1
        print(cur_i)
        return cur_i


        

