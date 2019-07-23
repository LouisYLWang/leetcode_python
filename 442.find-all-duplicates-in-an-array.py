#
# @lc app=leetcode id=442 lang=python
#
# [442] Find All Duplicates in an Array
#
class Solution(object):
    # self - implemented (slow with binary)
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        keeper = 0
        keeper_ = 0
        for i in nums:
            keeper |= 1 << (i - 1)
            keeper_ ^= 1 << (i - 1)
        target = keeper ^ keeper_
        i = 1
        res = list()
        while target != 0:
            if target & 1 == 1:
                res.append(i)
            target >>= 1 
            i += 1
        return res
