#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums:
            
            # find the interception of two sorted array
            l = 0
            r = n = len(nums)

            while l < r:
                m = (l + r)//2
                if nums[m] > nums[l]:
                    l = m
                else:
                    r = m

            cut = m
            # binary search in first array 

            l = 0
            r = cut

            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            
            if nums[l] == target:
                return l
            else:
                
                # binary search in second array 

                l = cut + 1 
                r = n - 1
                while l < r:
                    m = (l+r) // 2
                    print(l,r,m)
                    if nums[m] < target:
                        l = m + 1 
                    else:
                        r = m
                if l < n and nums[l] == target:
                    return l
                
        return -1
