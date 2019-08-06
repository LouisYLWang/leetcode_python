#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
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
            while target != 0:
                if target & 1 == 1:
                    return i
                target >>= 1 
                i += 1
        

