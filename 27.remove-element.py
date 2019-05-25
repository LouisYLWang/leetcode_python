#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_ix = 0
        while cur_ix < len(nums):
            if nums[cur_ix] == val:
                del nums[cur_ix]
            else:
                cur_ix += 1
        return cur_ix


