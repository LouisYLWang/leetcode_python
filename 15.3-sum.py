#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        
        if n < 3:
            return []
        
        nums.sort()
        #res = set()
        res = list()
        
        for i, a in enumerate(nums[:-2]):
            # i >= 1 to make sure if all element equal to each other
            # a == nums[i-1] to jump over same element
            if i >= 1 and a == nums[i-1]:
                continue
            
            l = i + 1
            r = n - 1
            
            while l < r:
                # using two pointer 
                if nums[l] + nums[r] + a == 0:
                    res.append([nums[l], nums[r], a])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                elif nums[l] + nums[r] + a > 0:
                    r -= 1
                else:
                    l += 1
                    
                
            '''
            # using hash
            visited = dict()
            for b in nums[i+1:]:
                if b not in visited:
                    # if -a-b appear again, get one result
                    visited[-a-b] = 1
                else:
                    res.add((a, b, -a-b))
            '''
        return res

