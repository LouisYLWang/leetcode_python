#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.res_ls = []
        cur_sum = 0
        for i in nums:
            cur_sum += i
            self.res_ls.append(cur_sum)        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.res_ls[j]
        return self.res_ls[j] - self.res_ls[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

