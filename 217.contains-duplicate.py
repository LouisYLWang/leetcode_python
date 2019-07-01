#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            nums_set.add(i)
        return False

