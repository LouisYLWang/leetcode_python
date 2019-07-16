#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #sorted version:
        nums1.sort()
        nums2.sort()
        len_1 = len(nums1)
        len_2 = len(nums2)
        i, j = 0,0 
        res = []
        while i < len_1 and j < len_2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            elif nums2[j] == nums1[i]:
                res.append(nums1[i])
                i += 1
                j += 1
        return res



