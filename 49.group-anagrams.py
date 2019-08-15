#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getHash(s):
            hash_ = [0]*26
            for i in s:
                hash_[ord(i) - ord('a')] += 1
            return str(hash_)
        
        str_map = dict()
        for s in strs:
            key = getHash(s)
            if key not in str_map:
                str_map[key] = list()
            str_map[key].append(s)
        
        return list(str_map.values())
            

