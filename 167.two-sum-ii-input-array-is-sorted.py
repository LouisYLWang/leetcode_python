#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -=1
            if numbers[i] + numbers[j] < target:
                i +=1
        return [i+1, j+1]


