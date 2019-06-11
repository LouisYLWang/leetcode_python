#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
class Solution:
    def merge(self, nums1, m, nums2, n):

        if not m:
            nums1[:] = nums2[:]
        else:
            while m > 0 and n > 0:
                if nums1[m-1] >= nums2[n-1]:
                    nums1[m+n-1], nums1[m-1] = nums1[m-1], nums1[m+n-1]
                    m -= 1
                else:
                    nums1[m+n-1], nums2[n-1] = nums2[n-1], nums1[m+n-1]
                    n -= 1
        nums1[:n] = nums2[:n]

