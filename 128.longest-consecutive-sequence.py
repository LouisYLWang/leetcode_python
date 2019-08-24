#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count_map = dict()
        for i in nums:
            if i not in count_map:
                count_map[i] = 0 


                if i - 1 in count_map:
                    count_map[i] += count_map[i - 1]


                if i + 1 in count_map:
                    count_map[i] += count_map[i + 1]

                count_map[i] += 1 

                if i - 1 in count_map:
                    if i-count_map[i-1] in count_map:
                        count_map[i - count_map[i-1]] = count_map[i]

                if i + 1 in count_map:
                    if i + count_map[i+1] in count_map:
                        count_map[i + count_map[i+1]] = count_map[i]


        return max(count_map.values())
