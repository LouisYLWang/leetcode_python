#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dp = {0:-1}
        cursum = 0
        i = 0
        n = len(nums)
        while i < n:
            cursum += nums[i]
            if k != 0:
                cursum = cursum % k
            
            if cursum in dp:
                if i - dp[cursum] > 1:
                    return True
            else:
                dp[cursum] = i
            i += 1
        return False
        
        
        
        # better not discuss cases separately
        '''
        if (k == 1 or k == -1) and len(nums) > 1:
            return True
        
        count_0 = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i +1] == 0:
                return True
        if k == 0:
            return False

        modhash = {0}
        cursum = 0

        for n in nums:
            cursum += n
            if cursum%k in modhash:
                return True
            else:
                modhash.add(cursum%k)
            print(modhash)
        return False
        '''
        
        
# @lc code=end

