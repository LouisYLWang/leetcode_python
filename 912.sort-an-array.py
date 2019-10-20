#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:

    # quick sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        nums_1 = list()
        nums_2 = list()
        t = nums[0]
        for num in nums[1:]:
            if num > t:
                nums_2.append(num)
            else:
                nums_1.append(num)
        res = self.sortArray(nums_1) 
        res.append(t)
        res += self.sortArray(nums_2)
        return res

    # merge sort
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        nums[n//2:]
        return self.merge(self.sortArray(nums[:n//2]), self.sortArray(nums[n//2:]))
    
    def merge(self, nums_1, nums_2):
        i = j = 0
        n = len(nums_1)
        m = len(nums_2)
        nums_1.append(50001)
        nums_2.append(50001)
        res = list()
        while len(res) < n + m:
            if nums_1[i] > nums_2[j]:
                res.append(nums_2[j])
                j = j + 1
            else:
                res.append(nums_1[i])
                i = i + 1
        return res
# @lc code=end

