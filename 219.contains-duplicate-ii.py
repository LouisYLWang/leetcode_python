#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#
# solution using single hashtable (but slow)
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        i = 0 
        index = {}

        while i < len(nums):
            cur = nums[i]
            
            if cur not in index:
                index[cur] = -i
            else:
                if index[cur] <= 0:
                    if i + index[cur] <= k:
                        return True 
                    else:index[cur] = i
                elif index[cur] > k:
                    if i - index[cur] <= k:
                        return True
                    else:index[cur] = i
            i += 1
            

        if max(index.values()) > k or max(index.values()) <= 0 :
            return False 
        return True

