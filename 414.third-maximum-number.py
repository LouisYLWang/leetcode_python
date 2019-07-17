#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tube = [-float("inf")] * 3

        for i in nums:
            if i not in tube:
                if i > tube[0]:
                    tube[0] = i
                    if i > tube[1]:
                        tube[0], tube[1] = tube[1], tube[0]
                    if i > tube[2]:
                        tube[1], tube[2] = tube[2], tube[1]

        if tube[0] == -float("inf"):
            return tube[2]
        return tube[0]

        #theoratical works but with not on special cases
        '''
        max_ = max(nums)
        min_ = min(nums)      
        bitmap = [0] * (max_ - min_ + 1)
        count = 0
        for i in nums:
            if bitmap[max_ - i] != 1:
                bitmap[max_ -i] += 1
                count += 1
        
        if count < 3:
            return max_
        
        else:
            i = 0
            find = 0
            while find < 3:
                if bitmap[i] == 1:
                    find += 1
                i += 1
            return max_ - i + 1
        '''

