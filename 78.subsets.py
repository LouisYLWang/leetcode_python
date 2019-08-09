#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_ele(set_hash, nums):
            #set_hash >>= 1
            k = 0
            res = list()
            while set_hash:
                if set_hash & 1:
                    res.append(nums[k])
                k += 1
                set_hash >>= 1
            return res
        
        ans = list()
        for i in range(1<<len(nums)):
            ans.append(get_ele(i,nums))
        return ans


