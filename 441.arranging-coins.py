#
# @lc app=leetcode id=441 lang=python
#
# [441] Arranging Coins
#
        
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = (left + right) //2
        while left < right-1:
            print(left, right, mid, mid * (mid + 1)//2 )
            if mid * (mid + 1)//2 < n:
                left = mid
            else:
                right = mid
            mid = (left + right) //2
        if n - mid * (mid + 1) //2 < mid + 1:
            return mid
        else:
            return mid + 1
