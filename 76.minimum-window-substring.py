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
        t_map = dict([[i, 0] for i in t]) 
        #print(t_map.keys())
        for i in t: t_map[i] += 1
        #print(t_map.values())
        left, right = 0, 0
        cache = t_map.copy()
        #counter = 0
        min_len = float("inf")
        res = ""
        while right < len(s):
            while max(cache.values()) > 0 and right < len(s):
                #print(right, s[right])
                if s[right] in cache:
                    cache[s[right]] -= 1
                #print(cache.values())
                #print(max(cache.values()))
                right += 1
                #counter += 1
            #print(s[left:right])
            i = left
            #print(right)
            
            
            while i < right:
                print(s[i],left,s[left],cache.values())
                if s[i] not in cache:
                    left += 1
                elif cache[s[i]] <0:
                    cache[s[i]] += 1
                    left += 1
                else:
                    break   
                i += 1
            

                #while cache[s[i]] <0:
                #    cache[s[i]] += 1
                #    left += 1
            
                #i += 1
                
                
                #print(s[i],left,s[left], cache[s[left]])
                #while cache[s[left]] <= 0:
                #    print(left)
                #    left += 1
                #i += 1
            if s[left:right]:
                if right - left < min_len:
                    res = s[left:right]
                    min_len = right - left
                #print(cur,s[left:right], min_len)
                #print("res:" + s[left:right])
                left = right
                cache = t_map.copy()
                counter = 0
        return res            
    
            #print(s[left:right])
            
            #print(s[i],left,s[left], s[i] in cache)
            #while s[i] not in cache:
                #print(s[i],left,s[left], s[i] in cache)
            #    i += 1
            #    left += 1
            #counter -= 1
        '''               
        while i < right:
            print(s[i],left,s[left], s[i] in cache, cache.values())
            #if s[i] not in cache:

            while s[i] not in t:
                print(s[i],left,s[left], s[i] in cache, cache.values())
                left += 1
                i += 1

            if cache[s[i]] < 0:
                left += 1
                cache[s[i]] += 1
            i += 1
            #else:
            #    left += 1
        '''       

      





        '''
        window = dict([[i, 0] for i in t])
        for i in t: window[i] += 1
        
        #window = dict([[i, 0] for i in t])
        res = ""    
        left, right = 0, 0
        counter = 0
        i = 0
        min_len = -float('inf')

        while right < len(s):
            if window[s[right]] > 0:
                counter -= 1
            window[s[right]] -= 1
            right += 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = t[left:right]
                if window[s[left]] == 0:
                    counter -= 1
                window[s[left]] += 1
                left += 1
        return res 
        '''

