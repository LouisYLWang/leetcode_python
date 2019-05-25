#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        cur_ix = 0
        nums_len = len(nums)
        while cur_ix < nums_len:
            if target <= nums[cur_ix]:
                return cur_ix
            else:
                cur_ix += 1
        return cur_ix


