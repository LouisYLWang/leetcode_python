#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:

    # intuitively, use l and m:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        
        
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return True
            
            while l < m and nums[l] == nums[m]:
                # skip if all the same before m
                l += 1

            if nums[l] == nums[m]:
                l = m + 1
                
            elif nums[l] < nums[m]:
                #left sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            elif nums[l] > nums[m]:
                #right sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
                    


    # use m and taget to separate if statement
    def search(self, nums: List[int], target: int) -> bool:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1 
        
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == target:
                return True
            while l < m and nums[l] == nums[m]: # tricky part
                l += 1
                
            if nums[m] < target:
                # target in [min, r]
                if nums[m] < nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
                
            if nums[m] > target:
                # target in [l, max]
                if nums[m] >= nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
        return False 

# @lc code=end

