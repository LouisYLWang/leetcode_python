#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = dict([[i, 0] for i in t]) 
        for i in t: target[i] += 1
        t_map = dict([[i, 0] for i in t]) 
        left, right = 0, 0
        count = len(t)
        min_len = float("inf")
        res = ""
        flag = False
        while right < len(s) + 1:
            if not flag:
                if right == len(s):
                    break
                if s[right] in t_map:
                    t_map[s[right]] += 1
                right += 1
                
            else:
                if right - left < min_len:
                    res = s[left:right]
                    min_len = right - left
                if s[left] in t_map:
                    t_map[s[left]] -= 1
                left += 1              
            flag = True
            for i in t_map:
                flag &= target[i] <= t_map[i]
        return res
            
        
        '''
        t_map = dict([[i, 0] for i in t]) 
        for i in t: t_map[i] += 1
        left, right = 0, 0
        cache = t_map.copy()
        min_len = float("inf")
        res = ""
        while right < len(s):
            while max(cache.values()) > 0:
                if s[right] in cache:
                    cache[s[right]] -= 1

                right += 1

            if max(cache.values()) <= 0:
                i = left

                while i < right:
                    if s[i] not in cache:
                        left += 1
                    else:
                        if cache[s[i]] <0:
                            cache[s[i]] += 1
                            left += 1
                        else:break   
                    i += 1

                if s[left:right]:
                    if right - left < min_len:
                        res = s[left:right]
                        min_len = right - left

                    cache = t_map.copy()
                    counter = 0
                    left = right
        return res            
        '''




