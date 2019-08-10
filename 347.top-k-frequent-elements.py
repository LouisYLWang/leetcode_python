#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()
        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else: freq_map[i] = 1
                
        most_freq = max(freq_map.values())
        freq_ls = list(list() for i in range(0, most_freq + 1))

        for num in freq_map:
            freq_ls[freq_map[num]].append(num)
        ans = []
        i = most_freq
        while k>0:
            cur = freq_ls[i]
            ans += cur
            i -= 1
            k -= len(cur)
            return ans 
