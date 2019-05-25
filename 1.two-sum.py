#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_cp = nums.copy()
        for i in nums:
            index_1 = None
            index_1 = nums_cp.index(i)
            nums_cp.pop(index_1)
            diff = target - i
            if  diff in nums_cp:
                index_1 = nums.index(i)
                index_2 = nums.index(diff,index_1+1)       
                return [index_1, index_2]


