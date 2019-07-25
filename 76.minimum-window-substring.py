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
        for i in t: t_map[i] += 1
        window_map = dict()
        left, right = 0, 0
        target = len(t_map)
        ans = float("inf"), None, None
        while right < len(s):
            char = s[right]

            if char not in window_map:
                window_map[char] = 0 
            window_map[char] += 1

            if char in t_map and window_map[char] == t_map[char]:
                target -= 1
            
            while left <= right and not target:
                char = s[left]

                if right - left + 1 < ans[0]:
                    ans =  right - left + 1, left, right

                window_map[char] -= 1
                if char in t_map and window_map[char] < t_map[char]:
                    target += 1

                left += 1
            right += 1
        #print(left, right, char,  target, window_map.keys(), window_map.values(), ans)
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

        #self implemented, slow
        '''
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
    




