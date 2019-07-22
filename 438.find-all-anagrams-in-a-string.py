#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        i = 0
        l_p = len(p)
        target = sum(map(ord, p))
        p_ls = list(p)
        p_ls.sort()
        #print(target)
        res = []
        while i < len(s):
            cur = s[i:i+l_p]
            #print(cur, sum(map(ord, cur)))
            if sum(map(ord, cur)) == target:
                cur_ls = list(cur)
                cur_ls.sort()            
                if cur_ls == p_ls:
                    res.append(i)
            i += 1
        return res


            

