#
# @lc app=leetcode id=665 lang=python
#
# [665] Non-decreasing Array
#
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        i = 0
        
        while i < len(nums) -1:
            if nums[i] > nums[i + 1]:
                flag += 1
                if i + 2 < len(nums):
                    if nums[i+1] < nums[i-1]:
                        return False
            i += 1
        return flag <= 1

    def checkPossibility(self, nums: List[int]) -> bool:
    	j = 0
    	for i in range(len(nums)-1):
    		if nums[i]-nums[i+1] > 0:
    			D = i
    			j += 1
    			if j == 2:
    				return False
    	if j == 0 or D == 0 or D == len(nums)-2:
    		return True
    	if (nums[D-1] <= nums[D] <= nums[D+2]) or (nums[D-1] <= nums[D+1] <= nums[D+2]):
    		return True
    	else:
    		return False

        

